// Конфигурация игры
var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

// Создаем игру
var game = new Phaser.Game(config);
var cat;
var coins = 0;
var coinsText;

// Загружаем картинки и звуки
function preload() {
    this.load.image('cat', 'assets/cat.png');
    this.load.image('bg', 'assets/bg.png');
}

// Создаем объекты на экране
function create() {
    // Фон
    this.add.image(400, 300, 'bg');

    // Котик
    cat = this.add.image(400, 300, 'cat').setInteractive();
    cat.setScale(0.5); // Уменьшаем размер

    // Текст с монетами
    coinsText = this.add.text(20, 20, 'Мяу-коины: 0', { 
        fontSize: '32px', 
        fill: '#FFD700' 
    });

    // Клик по котику = +1 монета
    cat.on('pointerdown', function() {
        coins++;
        coinsText.setText('Мяу-коины: ' + coins);
        this.scale.set(0.55); // Анимация увеличения
        setTimeout(() => cat.setScale(0.5), 100);
    }, this);
}

// Игровой цикл (пока не используем)
function update() { }