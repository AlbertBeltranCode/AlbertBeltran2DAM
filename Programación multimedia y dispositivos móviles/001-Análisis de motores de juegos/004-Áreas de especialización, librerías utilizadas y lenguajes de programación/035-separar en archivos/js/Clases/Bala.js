class Bala {
    constructor() {
        this.x = jugador.x;                          // La posición x inicial de la bala es la misma posición del jugador
        this.y = jugador.y;                          // La posición y inicial de la bala es la misma posición del jugador
        this.vy = 10;                                // A la bala se le da una velocidad inicial
        this.direccion = -1;                         // La dirección se establece en -1 para disparar hacia arriba
    }

    mueve() {                                       // Método que mueve la bala
        this.y += this.direccion * this.vy;        // Actualiza su posición
    }

    dibuja() {                                     // Método que dibuja la bala
        contexto.beginPath();
        contexto.arc(this.x - desfase_global_x, this.y, 10, 0, Math.PI * 2);
        contexto.fill();
    }
}