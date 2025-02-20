// Referencias a los lienzos y contextos
const bgCanvas = document.getElementById('backgroundCanvas');
const bgCtx = bgCanvas.getContext('2d');
const drawingCanvas = document.getElementById('drawingCanvas');
const ctx = drawingCanvas.getContext('2d');

// Variables de estado
let drawing = false;
let currentColor = document.getElementById('colorPicker').value;
let brushSize = document.getElementById('brushSize').value;
let isErasing = false;
let mode = 'free'; // 'free', 'circle', 'rectangle'
let startX, startY;
let history = [];
let historyStep = -1;
let zoomLevel = 1;
const canvasContainer = document.getElementById('canvasContainer');

// Cambiar modo de dibujo
function setMode(newMode) {
    mode = newMode;
}

// Actualizar color
function updateColor(color) {
    currentColor = color;
    isErasing = false;
}

// Actualizar grosor del pincel
function updateBrushSize(size) {
    brushSize = size;
}

// Alternar borrador (usa composición para borrar)
function toggleEraser() {
    isErasing = !isErasing;
}

// Guardar el estado actual del lienzo de dibujo para undo/redo
function saveState() {
    // Si se realizó un undo, recortamos la historia futura
    history = history.slice(0, historyStep + 1);
    history.push(drawingCanvas.toDataURL());
    historyStep++;
}

function undo() {
    if (historyStep > 0) {
        historyStep--;
        let canvasPic = new Image();
        canvasPic.src = history[historyStep];
        canvasPic.onload = function() {
            ctx.clearRect(0, 0, drawingCanvas.width, drawingCanvas.height);
            ctx.drawImage(canvasPic, 0, 0);
        }
    }
}

function redo() {
    if (historyStep < history.length - 1) {
        historyStep++;
        let canvasPic = new Image();
        canvasPic.src = history[historyStep];
        canvasPic.onload = function() {
            ctx.clearRect(0, 0, drawingCanvas.width, drawingCanvas.height);
            ctx.drawImage(canvasPic, 0, 0);
        }
    }
}

// Obtener posición del evento (para mouse y touch)
function getPos(e) {
    const rect = drawingCanvas.getBoundingClientRect();
    let x, y;
    if (e.touches && e.touches.length > 0) {
        x = e.touches[0].clientX - rect.left;
        y = e.touches[0].clientY - rect.top;
    } else {
        x = e.offsetX;
        y = e.offsetY;
    }
    return { x, y };
}

// Inicio de dibujo o acción según modo
function startDrawing(e) {
    e.preventDefault();
    const pos = getPos(e);
    startX = pos.x;
    startY = pos.y;
    drawing = true;
    if (mode === 'free') {
        ctx.beginPath();
        ctx.moveTo(pos.x, pos.y);
    }
}

// Dibujo en tiempo real
function draw(e) {
    if (!drawing) return;
    e.preventDefault();
    const pos = getPos(e);
    if (mode === 'free') {
        ctx.lineWidth = brushSize;
        ctx.lineCap = "round";
        if (isErasing) {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.strokeStyle = 'rgba(0,0,0,1)';
        } else {
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = currentColor;
        }
        ctx.lineTo(pos.x, pos.y);
        ctx.stroke();
    } else {
        // Para modos de forma, se muestra una previsualización borrando el trazo temporal
        ctx.clearRect(0, 0, drawingCanvas.width, drawingCanvas.height);
        if (historyStep >= 0) {
            let canvasPic = new Image();
            canvasPic.src = history[historyStep];
            canvasPic.onload = function() {
                ctx.drawImage(canvasPic, 0, 0);
                drawShape(startX, startY, pos.x, pos.y);
            }
        } else {
            drawShape(startX, startY, pos.x, pos.y);
        }
    }
}

// Finalizar dibujo o acción
function endDrawing(e) {
    if (!drawing) return;
    e.preventDefault();
    drawing = false;
    if (mode === 'free') {
        saveState();
    } else if (mode === 'circle' || mode === 'rectangle') {
        const pos = getPos(e);
        drawShape(startX, startY, pos.x, pos.y);
        saveState();
    }
}

// Dibujar formas (círculo o rectángulo)
function drawShape(x1, y1, x2, y2) {
    ctx.lineWidth = brushSize;
    ctx.lineCap = "round";
    ctx.globalCompositeOperation = 'source-over';
    ctx.strokeStyle = currentColor;
    if (mode === 'circle') {
        let radius = Math.hypot(x2 - x1, y2 - y1);
        ctx.beginPath();
        ctx.arc(x1, y1, radius, 0, 2 * Math.PI);
        ctx.stroke();
    } else if (mode === 'rectangle') {
        ctx.beginPath();
        ctx.rect(x1, y1, x2 - x1, y2 - y1);
        ctx.stroke();
    }
}

// Asignar eventos a la capa de dibujo (sin funcionalidad de texto)
drawingCanvas.addEventListener('mousedown', startDrawing);
drawingCanvas.addEventListener('mousemove', draw);
drawingCanvas.addEventListener('mouseup', endDrawing);
drawingCanvas.addEventListener('mouseout', endDrawing);
drawingCanvas.addEventListener('touchstart', startDrawing);
drawingCanvas.addEventListener('touchmove', draw);
drawingCanvas.addEventListener('touchend', endDrawing);
drawingCanvas.addEventListener('touchcancel', endDrawing);

// Establecer el color de fondo en la capa de fondo
function setBackground() {
    const bgColor = document.getElementById('bgColorPicker').value;
    bgCtx.fillStyle = bgColor;
    bgCtx.fillRect(0, 0, bgCanvas.width, bgCanvas.height);
}

// Actualizar zoom aplicando una transformación CSS al contenedor
function updateZoom(value) {
    zoomLevel = value / 100;
    canvasContainer.style.transform = `scale(${zoomLevel})`;
}

// Inicializar fondo y guardar estado inicial
setBackground();
saveState();
