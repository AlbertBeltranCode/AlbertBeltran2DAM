(function (global) {
  const JocarsaFloralwhite = {};

  JocarsaFloralwhite.createSankeyChart = function(config) {
    const {
      element,
      data,
      width,
      height,
      nodeWidth = 20,
      nodePadding = 10
    } = config;

    let container;
    if (typeof element === 'string') {
      container = document.querySelector(element);
    } else {
      container = element;
    }
    if (!container) {
      throw new Error("Container element not found");
    }

    container.innerHTML = '';

    const svg = createSVGElement('svg');
    svg.setAttribute('width', width);
    svg.setAttribute('height', height);
    svg.classList.add('jocarsa-floralwhite-svg');
    container.appendChild(svg);

    const defs = createSVGElement('defs');
    svg.appendChild(defs);
    JocarsaFloralwhite.svgDefs = defs;

    const nodes = data.nodes.map((d, i) => {
      return {
        index: i,
        name: d.name || `Node ${i}`,
        color: d.color || getRandomColor(),
      };
    });

    const nameToIndex = {};
    nodes.forEach((node, i) => {
      nameToIndex[node.name] = i;
    });

    const links = data.links.map(link => {
      let sourceIndex, targetIndex;

      if (typeof link.source === 'string') {
        sourceIndex = nameToIndex[link.source];
        if (sourceIndex === undefined) {
          throw new Error(`Source node "${link.source}" not found in nodes array`);
        }
      } else {
        sourceIndex = link.source;
      }

      if (typeof link.target === 'string') {
        targetIndex = nameToIndex[link.target];
        if (targetIndex === undefined) {
          throw new Error(`Target node "${link.target}" not found in nodes array`);
        }
      } else {
        targetIndex = link.target;
      }

      return {
        source: sourceIndex,
        target: targetIndex,
        value: +link.value
      };
    });

    nodes.forEach(n => {
      n.sourceLinks = [];
      n.targetLinks = [];
      n.valueIn = 0;
      n.valueOut = 0;
      n.linkOffsetOut = 0;
      n.linkOffsetIn = 0;
    });

    links.forEach(link => {
      const s = nodes[link.source];
      const t = nodes[link.target];
      s.sourceLinks.push(link);
      t.targetLinks.push(link);
      s.valueOut += link.value;
      t.valueIn += link.value;
    });

    const sourceNodes = nodes.filter(n => n.valueIn === 0);
    assignNodeLayers(nodes, sourceNodes);

    const maxLayer = Math.max(...nodes.map(d => d.layer));
    const layerCount = maxLayer + 1;

    const xScale = (width - nodeWidth) / maxLayer;
    nodes.forEach(n => {
      n.x0 = n.layer * xScale;
      n.x1 = n.x0 + nodeWidth;
    });

    const layers = [];
    for (let i = 0; i <= maxLayer; i++) {
      layers[i] = [];
    }
    nodes.forEach(n => {
      layers[n.layer].push(n);
    });
    layers.forEach(layerNodes => {
      layerNodes.sort((a, b) => b.valueOut - a.valueOut);
      distributeLayerNodes(layerNodes, height, nodePadding);
    });

    const tooltip = document.createElement('div');
    tooltip.classList.add('tooltip');
    document.body.appendChild(tooltip);

    function showTooltip(text, event) {
      tooltip.textContent = text;
      tooltip.style.opacity = 1;
      tooltip.style.left = `${event.pageX + 5}px`;
      tooltip.style.top = `${event.pageY + 5}px`;
    }

    function hideTooltip() {
      tooltip.style.opacity = 0;
    }

    links.forEach((link, idx) => {
      const source = nodes[link.source];
      const target = nodes[link.target];

      const linkWidthScale = (source.y1 - source.y0 - (source.sourceLinks.length - 1) * nodePadding) /
                             source.sourceLinks.reduce((sum, l) => sum + l.value, 0);

      const linkHeight = link.value * linkWidthScale;

      const sy0 = source.y0 + source.linkOffsetOut + linkHeight / 2;
      source.linkOffsetOut += linkHeight + nodePadding;

      const ty0 = target.y0 + target.linkOffsetIn + linkHeight / 2;
      target.linkOffsetIn += linkHeight + nodePadding;

      let linkStroke;
      if (source.color === target.color) {
        linkStroke = source.color;
      } else {
        const gradientId = `gradient-${source.index}-${target.index}`;
        let linearGradient = defs.querySelector(`#${gradientId}`);
        if (!linearGradient) {
          linearGradient = createSVGElement('linearGradient');
          linearGradient.setAttribute('id', gradientId);
          linearGradient.setAttribute('x1', '0%');
          linearGradient.setAttribute('y1', '0%');
          linearGradient.setAttribute('x2', '100%');
          linearGradient.setAttribute('y2', '0%');

          const stop1 = createSVGElement('stop');
          stop1.setAttribute('offset', '0%');
          stop1.setAttribute('stop-color', source.color);
          linearGradient.appendChild(stop1);

          const stop2 = createSVGElement('stop');
          stop2.setAttribute('offset', '100%');
          stop2.setAttribute('stop-color', target.color);
          linearGradient.appendChild(stop2);

          defs.appendChild(linearGradient);
        }

        linkStroke = `url(#${gradientId})`;
      }

      const path = createSVGElement('path');
      path.setAttribute('class', 'jocarsa-floralwhite-link');
      path.setAttribute('d', sankeyLinkPath(
        source.x1, sy0,
        target.x0, ty0
      ));
      path.setAttribute('stroke', linkStroke);
      path.setAttribute('stroke-width', linkHeight);
      path.setAttribute('fill', 'none');

      path.addEventListener('mouseover', (event) => {
        path.style.strokeOpacity = 0.7;
        showTooltip(`Link: ${source.name} -> ${target.name}\nValue: ${link.value}`, event);
      });
      path.addEventListener('mouseout', () => {
        path.style.strokeOpacity = 0.2;
        hideTooltip();
      });

      svg.appendChild(path);
    });

    nodes.forEach(node => {
      const g = createSVGElement('g');
      g.setAttribute('class', 'jocarsa-floralwhite-node');

      const rect = createSVGElement('rect');
      rect.setAttribute('x', node.x0);
      rect.setAttribute('y', node.y0);
      rect.setAttribute('width', nodeWidth);
      rect.setAttribute('height', node.y1 - node.y0);
      rect.setAttribute('fill', node.color);
      rect.setAttribute('stroke', '#ffffff');
      rect.setAttribute('rx', 5);
      rect.setAttribute('ry', 5);
      rect.setAttribute('stroke-width', 2);
      rect.classList.add('jocarsa-floralwhite-rect');

      rect.addEventListener('mouseover', (event) => {
        rect.style.fill = 'orange';
        showTooltip(`Node: ${node.name}\nIn: ${node.valueIn}\nOut: ${node.valueOut}`, event);
      });
      rect.addEventListener('mouseout', () => {
        rect.style.fill = node.color;
        hideTooltip();
      });

      rect.addEventListener('click', (event) => {
        event.stopPropagation();
        const colorPicker = createColorPicker(node);
        colorPicker.click();
      });

      g.appendChild(rect);

      const text = createSVGElement('text');
      text.setAttribute('x', node.x0 + nodeWidth / 2);
      text.setAttribute('y', node.y0 + (node.y1 - node.y0) / 2);
      text.setAttribute('dy', '0.35em');
      text.setAttribute('text-anchor', 'middle');
      text.textContent = node.name;
      text.classList.add('jocarsa-floralwhite-text');
      g.appendChild(text);

      svg.appendChild(g);
    });

    let zoom = d3.zoom()
      .scaleExtent([0.5, 5])
      .on('zoom', (event) => {
        svg.selectAll('g')
          .attr('transform', event.transform);
      });

    svg.call(zoom);

    JocarsaFloralwhite.currentNodes = nodes;

    const legendButton = document.getElementById('toggle-legend-btn');
    legendButton.addEventListener('click', () => {
      JocarsaFloralwhite.toggleLegend();
    });
  };

  function assignNodeLayers(nodes, sourceNodes) {
    nodes.forEach(n => n.layer = undefined);

    const queue = [];
    sourceNodes.forEach(s => {
      s.layer = 0;
      queue.push(s);
    });

    while (queue.length) {
      const current = queue.shift();
      const currentLayer = current.layer;
      current.sourceLinks.forEach(link => {
        const targetNode = nodes[link.target];
        if (targetNode.layer == null || targetNode.layer < currentLayer + 1) {
          targetNode.layer = currentLayer + 1;
          queue.push(targetNode);
        }
      });
    }
  }

  function distributeLayerNodes(layerNodes, totalHeight, nodePadding) {
    if (!layerNodes.length) return;
    const totalValue = layerNodes.reduce((sum, n) => sum + Math.max(n.valueIn, n.valueOut), 0);
    let yStart = 0;

    layerNodes.forEach(n => {
      const nodeValue = Math.max(n.valueIn, n.valueOut);
      const nodeHeight = (nodeValue / totalValue) * (totalHeight - nodePadding * (layerNodes.length - 1));
      n.y0 = yStart;
      n.y1 = yStart + nodeHeight;
      yStart += nodeHeight + nodePadding;
    });
  }

  function sankeyLinkPath(x0, y0, x1, y1) {
    const curvature = 0.5;
    const xi = d3InterpolateNumber(x0, x1);
    const x2 = xi(curvature);
    const x3 = xi(1 - curvature);
    return `M${x0},${y0} C${x2},${y0} ${x3},${y1} ${x1},${y1}`;
  }

  function d3InterpolateNumber(a, b) {
    return function(t) {
      return a + (b - a) * t;
    };
  }

  function createSVGElement(name) {
    return document.createElementNS('http://www.w3.org/2000/svg', name);
  }

  function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function createColorPicker(node) {
    const colorPicker = document.createElement('input');
    colorPicker.type = 'color';
    colorPicker.value = node.color;
    colorPicker.addEventListener('input', (event) => {
      const newColor = event.target.value;
      node.color = newColor;
      document.querySelector(`#legend-container`).style.display = 'block';
      JocarsaFloralwhite.updateLegendContent();
      JocarsaFloralwhite.updateLinkGradients();
      document.querySelectorAll('.jocarsa-floralwhite-rect').forEach(rect => {
        if (rect.__data__.name === node.name) {
          rect.setAttribute('fill', newColor);
        }
      });
    });
    document.body.appendChild(colorPicker);
    return colorPicker;
  }

  JocarsaFloralwhite.updateLegendContent = function(){
    let legend = document.getElementById('legend-container');
    if(legend && JocarsaFloralwhite.currentNodes){
      let legendContent = '<h3>Leyenda</h3><ul>';
      JocarsaFloralwhite.currentNodes.forEach(node => {
        legendContent += `<li><span style="display:inline-block;width:12px;height:12px;background:${node.color};margin-right:5px;"></span>${node.name}</li>`;
      });
      legendContent += '</ul>';
      legend.innerHTML = legendContent;
    }
  };

  JocarsaFloralwhite.toggleLegend = function(){
    let legend = document.getElementById('legend-container');
    if(legend){
      legend.style.display = (legend.style.display === 'none' ? 'block' : 'none');
    } else {
      legend = document.createElement('div');
      legend.id = 'legend-container';
      legend.style.position = 'absolute';
      legend.style.top = '50px';
      legend.style.right = '10px';
      legend.style.backgroundColor = '#fff';
      legend.style.border = '1px solid #ccc';
      legend.style.padding = '10px';
      legend.style.zIndex = '1000';
      let legendContent = '<h3>Leyenda</h3><ul>';
      if(JocarsaFloralwhite.currentNodes){
        JocarsaFloralwhite.currentNodes.forEach(node => {
          legendContent += `<li><span style="display:inline-block;width:12px;height:12px;background:${node.color};margin-right:5px;"></span>${node.name}</li>`;
        });
      }
      legendContent += '</ul>';
      legend.innerHTML = legendContent;
      document.body.appendChild(legend);
    }
  };

  JocarsaFloralwhite.updateLinkGradients = function(){
    if(JocarsaFloralwhite.svgDefs && JocarsaFloralwhite.currentNodes){
      const gradients = JocarsaFloralwhite.svgDefs.querySelectorAll('linearGradient');
      gradients.forEach(gradient => {
        const parts = gradient.id.split('-');
        if(parts.length >= 3){
          const sourceIndex = parseInt(parts[1], 10);
          const targetIndex = parseInt(parts[2], 10);
          if(!isNaN(sourceIndex) && !isNaN(targetIndex)){
            const sourceNode = JocarsaFloralwhite.currentNodes[sourceIndex];
            const targetNode = JocarsaFloralwhite.currentNodes[targetIndex];
            const stops = gradient.querySelectorAll('stop');
            if(stops.length >= 2){
              stops[0].setAttribute('stop-color', sourceNode.color);
              stops[1].setAttribute('stop-color', targetNode.color);
            }
          }
        }
      });
    }
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = JocarsaFloralwhite;
  } else {
    global.jocarsaFloralwhite = JocarsaFloralwhite;
  }

})(this);
