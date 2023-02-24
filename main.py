@namespace
class SpriteKind:
    entity = SpriteKind.create()
    things = SpriteKind.create()
    pave = SpriteKind.create()
    slowdown = SpriteKind.create()
    l2sprites = SpriteKind.create()
    l2car = SpriteKind.create()
    l2safe = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Explosion, x, pavement2, pavement, p, ha, y, PSAI, deron, yash, zeal, d
    sprites.destroy(Car1)
    sprites.destroy(Car2)
    Explosion = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 4 4 4 4 4 . . . . . . 
                    . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                    . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                    . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                    . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                    . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                    . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                    . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                    . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                    . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                    . . . 2 2 4 d 5 5 d d 4 4 . . . 
                    . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                    . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                    . . . . . 2 2 2 2 2 2 . . . . .
        """),
        SpriteKind.entity)
    Explosion.set_position(75, 95)
    animation.run_image_animation(Explosion,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 4 4 4 4 4 . . . . . . 
                        . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                        . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                        . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                        . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                        . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                        . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                        . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                        . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                        . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                        . . . 2 2 4 d 5 5 d d 4 4 . . . 
                        . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                        . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                        . . . . . 2 2 2 2 2 2 . . . . .
            """),
            img("""
                . . . . 2 2 2 2 2 2 2 2 . . . . 
                        . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                        . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                        . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                        . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                        2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                        2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                        4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                        . . b b b b 2 4 4 2 b b b b . . 
                        . b d d d d 2 4 4 2 d d d d b . 
                        b d d b b b 2 4 4 2 b b b d d b 
                        b d d b b b b b b b b b b d d b 
                        b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                        . . b b d d 1 1 3 d d 1 b b . . 
                        . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                        . . . 2 2 4 4 4 4 4 2 2 2 . . .
            """),
            img("""
                . . . . . . . . b b . . . . . . 
                        . . . . . . . . b b . . . . . . 
                        . . . b b b . . . . . . . . . . 
                        . . b d d b . . . . . . . b b . 
                        . b d d d b . . . . . . b d d b 
                        . b d d b . . . . b b . b d d b 
                        . b b b . . . . . b b . . b b . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . b b b d d d d d d b b b . . 
                        . b d c c c b b b b c c d d b . 
                        b d d c b . . . . . b c c d d b 
                        c d d b b . . . . . . b c d d c 
                        c b d d d b b . . . . b d d c c 
                        . c c b d d d d b . c c c c c c 
                        . . . c c c c c c . . . . . . .
            """)],
        100,
        False)
    pause(500)
    sprites.destroy(Explosion, effects.fire, 100)
    pause(2000)
    x = 1
    if x == 1:
        sprites.destroy(Explosion, effects.fire, 200)
        game.show_long_text("Now, We have discovered a way to stop accidents like this.",
            DialogLayout.FULL)
        game.show_long_text("To demonstrate this, The player will be driving a car with 'A' button and stop with 'B'",
            DialogLayout.FULL)
        game.show_long_text("And when the light at the corner turns red, stop and when the light turns green it Go!",
            DialogLayout.FULL)
        game.show_long_text("You are the Red Car!", DialogLayout.FULL)
        scene.set_background_image(img("""
            7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffff
                        77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff11
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff11ff
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffffffffff
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffffffffffffff
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111ffffffffff
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111fffffffffffff
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111ffffffffffffffff
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111fffffffffffffffffff
                        777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffff
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffff77
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff11fffffffffffffffffffffffffffffffff777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffff777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff777777777777
                        77777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7777777777777777
                        77777777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff777777777777777777
                        77777777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff11fffffffffffffffffffffffffffffffff77777777777777777777
                        77777777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffff77777777777777777777777
                        77777777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffff7777777777777777777777777
                        77777777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffff7777777777777777777777777777
                        77777777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7777777777777777777777777777777
                        77777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7777777777777777777777777777777777
                        777777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff777777777777777777777777777777777777
                        777777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffff777777777777777777777777777777777777777
                        777777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffff777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777fffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777777ffffffffffffffffffffffffffffffff11ffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777fffffffffffffffffffffff111ffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777fffffffffffffffffffff11ffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777ffffffffffffffffff111ffffffffffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777fffffffffffffff111ffffffffffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffff111ffffffffffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11ffffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11ffffffffffffffffff7777777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffff777777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffff77777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffff777777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffffff7777777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffffff77777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffffff777777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffff777777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffff7777777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffff777777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffff7777777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffff77777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffff777777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffff11fffffffffffffffffffff7777777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffff77777777777777777777777777777
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff11fffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffff1ffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffff1111111111fffff1111111111
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        """))
        pavement2 = sprites.create(img("""
                .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            .............................................
                            f............................................
                            .f...........................................
                            ..f..........................................
                            ..ff.........................................
                            ....f........................................
                            .....ff......................................
                            .......f.....................................
                            ........ff...................................
                            .........f...................................
                            ..........ff.................................
                            ...........ff................................
                            .............f...............................
                            ..............f..............................
                            ...............f.............................
                            ................ff...........................
                            .................ff..........................
                            ...................ff........................
                            .....................ff......................
                            ......................ff.....................
                            ........................ff...................
                            ..........................ff.................
                            ...........................ff................
                            .............................ff..............
                            ..............................fff............
                            ................................ff...........
                            .................................ff..........
                            ...................................ff........
                            ......................................f......
                            .............................................
                            .............................................
                            .............................................
                            .............................................
            """),
            SpriteKind.pave)
        pavement2.set_position(117, 95)
        pavement = sprites.create(img("""
                f . . . . . . . . . . . . . . . 
                            f f . . . . . . . . . . . . . . 
                            . f f . . . . . . . . . . . . . 
                            . . f f . . . . . . . . . . . . 
                            . . . f f f . . . . . . . . . . 
                            . . . . . f f f . . . . . . . . 
                            . . . . . . . f f . . . . . . . 
                            . . . . . . . . f f . . . . . . 
                            . . . . . . . . . f f . . . . . 
                            . . . . . . . . . . f f . . . . 
                            . . . . . . . . . . . f f . . . 
                            . . . . . . . . . . . . f f . . 
                            . . . . . . . . . . . . . f f . 
                            . . . . . . . . . . . . . . f . 
                            . . . . . . . . . . . . . . f f 
                            . . . . . . . . . . . . . . . f
            """),
            SpriteKind.pave)
        pavement.set_position(81, 82)
        p = sprites.create(img("""
                . . . . . . . e e e e e . . . . 
                            . . . . . e e 2 2 2 2 2 e . . . 
                            . . . . e e 2 2 2 2 2 2 2 e . . 
                            . . . . e 9 4 4 4 2 2 2 4 b e . 
                            . . e e 9 9 4 4 4 4 2 2 4 9 b e 
                            . e 2 2 9 9 4 4 4 4 4 2 4 9 9 e 
                            e 2 2 2 9 9 2 4 4 4 4 4 2 9 9 e 
                            e 2 2 2 9 9 e e e e e e e 9 9 e 
                            e 2 2 2 9 b e b b b e b e b 9 e 
                            e 2 e e e e b b b b e b b e b e 
                            e e 3 3 e e 2 2 2 2 e 2 2 e e e 
                            e 3 3 e e e e e e e e e e e e e 
                            e e e e e e e e e e e e e e e e 
                            e e e e f f f e e e e f f f e e 
                            . e e f f f b f e e f f f b f . 
                            . . . . c b b . . . . c b b . .
            """),
            SpriteKind.player)
        p.set_position(132, 97)
        ha = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . 6 6 6 6 6 6 6 6 . . 
                            . . . . . 6 c 6 6 6 6 6 6 9 6 . 
                            . . . . 6 c c 6 6 6 6 6 6 9 c 6 
                            . . d 6 9 c c 6 9 9 9 9 9 9 c c 
                            . d 6 6 9 c b 8 8 8 8 8 8 8 6 c 
                            . 6 6 6 9 b 8 8 b b b 8 b b 8 6 
                            . 6 6 6 6 6 8 b b b b 8 b b b 8 
                            . 6 6 6 6 8 6 6 6 6 6 8 6 6 6 8 
                            . 6 d d 6 8 f 8 8 8 f 8 8 8 8 8 
                            . d d 6 8 8 8 f 8 8 f 8 8 8 8 8 
                            . 8 8 8 8 8 8 8 f f f 8 8 8 8 8 
                            . 8 8 8 8 f f f 8 8 8 8 f f f f 
                            . . . 8 f f f f f 8 8 f f f f f 
                            . . . . f f f f . . . . f f f . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.entity)
        y = 1
        ha.set_position(149, 21)
        PSAI = sprites.create(img("""
                f f f f f f f f f f f f f f f f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f 7 f f f f 7 7 f f f f f f 7 f 
                            f 7 f 7 7 7 7 7 f 7 7 7 7 f 7 f 
                            f 7 f 7 7 7 7 7 f 7 7 7 7 f 7 f 
                            f 7 f 7 f f 7 7 f 7 7 7 7 f 7 f 
                            f 7 f 7 7 f 7 7 f 7 7 7 7 f 7 f 
                            f 7 f f f f 7 7 f f f f f f 7 f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                            f f f f f f f f f f f f f f f f
            """),
            SpriteKind.player)
        PSAI.set_position(24, 63)
        pause(500)
        ha.set_velocity(-30, 10)
        deron = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . f . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.things)
        deron.set_position(95, 41)
        yash = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . f . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.things)
        yash.set_position(44, 62)
        zeal = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . f . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.things)
        zeal.set_position(125, 100)
        d = 1
sprites.on_overlap(SpriteKind.entity, SpriteKind.entity, on_on_overlap)

def on_b_pressed():
    global l2back, safe, l2Zeal, l2shooter, l2shooter2, l2shooter3, pcm, selection
    if selection == 1:
        scene.set_background_image(img("""
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        """))
        l2back = sprites.create(img("""
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999994444444444499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999999445555555555544999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999944555555555555555449999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999999455555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999994555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999945555555555555555555555549999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            9999999455555555555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            999999945555555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999c
                            99999945555555555555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999ce
                            9999994555555555555555555555555555499999999999999999999999999999999c99999999999999999999999999999999999999999999cc99999999999999999999999999999999999999999999ce
                            999994555555555555555555555555555554999999999999999999999999999999cec999999999999999999999999999999999999999999cec99999999999999999999999999999999999999999999ce
                            999994555555555555555555555555555554999999999999999999999999999999cec999999999999999999999999999999999999999999cec9999999999999999999999999999999999999999999cee
                            999994555555555555555555555555555554999999999999999999999999999999ceec99999999999999999999999999999999999999999ceec999999999999999999999999999999999999999999cee
                            99999455555555555555c55555555555555499999999999999999999999999999ceeec9999999999999999999999999999999999999999ceeec99999999999999999999999999999999999999999ceee
                            9999945555555555555cec5555555555555499999999999999999999999999999ceeec9999999999999999999999999999999999999999ceeeec9999999999999999999999999999999999999999ceee
                            999994555555555555ceec555555555555549999999999999999999999999999ceeeeec999999999999999999999999999999999999999ceeeec9999999999999999999999999999999999999999ceee
                            99999455555555555ceeeec55555555555549999999999999999999999999999ceeeeec99999999999999999999999999999999999999ceeeeec999999999999999999999999999999999999999ceeee
                            99999455555555555ceeeeec5555555555549999999999999999999999999999ceeeeeec9999999999999999999999999999999999999ceeeeeec99999999999999999999999999999999999999ceeee
                            99999455555555555ceeeeec555555555554999999999999999999999999999ceeeeeeec9999999999999999999999999999999999999ceeeeeec9999999999999999999999999999999999999ceeeee
                            9999945555555555ceeeeeeec55555555554999999999999999999999999999ceeeeeeec999999999999999999999999999999999999ceeeeeeec9999999999999999999999999999999999999ceeeee
                            9999945555555555ceeeeeeec5555555555499999999999999999999999999ceeeeeeeeec99999999999999999999999999999999999ceeeeeeeec999999999999999999999999999999999999ceeeee
                            9999994555555555ceeeeeeeec555555554999999999999999999999999999ceeeeeeeeec99999999999999999999999999999999999ceeeeeeeec99999999999999999999999999999999999ceeeeee
                            999999455555555ceeeeeeeeec555555554999999999999999999999999999ceeeeeeeeeec999999999999999999999999999999999ceeeeeeeeeec9999999999999999999999999999999999ceeeeee
                            999999945555555ceeeeeeeeec55555554999999999999999999999999999ceeeeeeeeeeec999999999999999999999999999999999ceeeeeeeeeec9999999999999999999999999999999999ceeeeee
                            999999945555555ceeeeeeeeeec5555554999999999999999999999999999ceeeeeeeeeeeec99999999999999999999999999999999ceeeeeeeeeec999999999999999999999999999999999ceeeeeee
                            99999999455555ceeeeeeeeeeec555554999999999999999999999999999ceeeeeeeeeeeeec9999999999999999999999999999999ceeeeeeeeeeeec99999999999999999999999999999999ceeeeeee
                            99999999945555ceeeeeeeeeeeec55549999999999999999999999999999ceeeeeeeeeeeeec9999999999999999999999999999999ceeeeeeeeeeeec9999999999999999999999999999999ceeeeeeee
                            99999999994555ceeeeeeeeeeeec55499999999999999999999999999999ceeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeeeeeeec9999999999999999999999999999999ceeeeeeee
                            9999999999944ceeeeeeeeeeeeec4499999999999999999999999999999ceeeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeeeeeeeec999999999999999999999999999999ceeeeeeee
                            9999999999999ceeeeeeeeeeeeeec999999999999999999999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeee
                            999999999999ceeeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeee
                            999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeee
                            999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeee
                            99999999999ceeeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeee
                            99999999999ceeeeeeeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeee
                            99999999999ceeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeee
                            9999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeee
                            9999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeee
                            9999999999ceeeeeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeee
                            999999999ceeeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeee
                            999999999ceeeeeeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeee
                            999999999ceeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeee
                            99999999ceeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeee
                            99999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeee
                            99999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeee
                            9999999ceeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeee
                            9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeee
                            9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeee
                            999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeee
                            999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeee
                            999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeee
                            99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeee
                            99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeee
                            99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeee
                            9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeee
                            9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeee
                            999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeee
                            999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeee
                            999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeee
                            997777777777777777777777777777777777777ec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeee
                            9977eeee7777ee77777eeee7777eeeee7777777ec99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeee
                            9977e7777777eee7777e7777777e77777777777eec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeee
                            9c77ee777777e7e7777eee77777e77777777777eec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeee
                            9c777eee777eeeee777e7777777eeee77777777eeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999ceeeeeeeeeeeeeeeeeeeeee
                            9c77777e777e777ee77e7777777e77777777777eeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999ceeeeeeeeeeeeeeeeeeeeee
                            ce77777e77ee7777e77e7777777e77777777777eeec9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeee
                            ce7eeeee77777777777e7777777eeeee7777777eeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeee
                            ce7777777777777777777777777777777777777eeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeeeeeeeeeeeeeeeeeeee
                            1177777777777777777777777777777777777771111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                            bb7777eeee77eeeee77ee77e777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bb777777ee77e777e77ee77e777e77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bb77777ee777e777e77e7e7e777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bb7777ee7777e777e77e7eee777e77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bb7777eeee77eeeee77e77ee777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bb7777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111b
                            bbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111b
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                            dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
            """),
            SpriteKind.l2sprites)
        safe = sprites.create(img("""
                ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            .............................................................9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.............................................................
                            .............................................................7777777777777777777777777777777777777e.............................................................
                            .............................................................77eeee7777ee77777eeee7777eeeee7777777e.............................................................
                            .............................................................77e7777777eee7777e7777777e77777777777e.............................................................
                            .............................................................77ee777777e7e7777eee77777e77777777777e.............................................................
                            .............................................................777eee777eeeee777e7777777eeee77777777e.............................................................
                            .............................................................77777e777e777ee77e7777777e77777777777e.............................................................
                            .............................................................77777e77ee7777e77e7777777e77777777777e.............................................................
                            .............................................................7eeeee77777777777e7777777eeeee7777777e.............................................................
                            .............................................................7777777777777777777777777777777777777e.............................................................
                            .............................................................77777777777777777777777777777777777771.............................................................
                            .............................................................7777eeee77eeeee77ee77e777eeee77777777b.............................................................
                            .............................................................777777ee77e777e77ee77e777e77777777777b.............................................................
                            .............................................................77777ee777e777e77e7e7e777eeee77777777b.............................................................
                            .............................................................7777ee7777e777e77e7eee777e77777777777b.............................................................
                            .............................................................7777eeee77eeeee77e77ee777eeee77777777b.............................................................
                            .............................................................7777777777777777777777777777777777777b.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            .............................................................bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbb.............................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
            """),
            SpriteKind.l2safe)
        l2Zeal = sprites.create(img("""
                . . . . . . . 8 8 8 8 8 . . . . 
                            . . . . . 8 8 6 6 6 6 6 8 . . . 
                            . . . . 8 8 6 6 6 6 6 6 6 8 . . 
                            . . . . 8 9 7 6 6 6 6 6 7 b 8 . 
                            . . 8 8 9 9 7 7 6 6 6 6 7 9 b 8 
                            . 8 6 6 9 9 7 7 7 6 6 6 7 9 9 8 
                            8 6 6 6 9 9 6 7 7 7 7 7 6 9 9 8 
                            8 6 6 6 9 9 8 8 8 8 8 8 8 9 9 8 
                            8 6 6 6 9 b 8 b b b 8 b 8 b 9 8 
                            8 6 8 8 8 8 b b b b 8 b b 8 b 8 
                            8 8 3 3 8 8 6 6 6 6 8 6 6 8 8 8 
                            8 3 3 8 8 8 8 8 8 8 8 8 8 8 8 8 
                            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                            8 8 8 8 4 f f 8 8 8 8 f 4 f 8 8 
                            . 8 8 f 4 2 4 f 8 8 f 2 4 4 f . 
                            . . . . 2 2 4 . . . . 4 2 2 . .
            """),
            SpriteKind.l2car)
        l2shooter = sprites.create(img("""
                .........................................................99999999999999999......................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
            """),
            SpriteKind.l2sprites)
        l2shooter2 = sprites.create(img("""
                .........................................................99999999999999999......................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
            """),
            SpriteKind.l2sprites)
        l2shooter3 = sprites.create(img("""
                .........................................................99999999999999999......................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
                            ................................................................................................................................................................
            """),
            SpriteKind.l2sprites)
        l2shooter.set_position(78, 3)
        safe.set_position(19, 88)
        l2shooter2.set_position(45, 3)
        l2shooter3.set_position(106, 2)
        controller.move_sprite(l2Zeal, 300, 200)
        l2Zeal.set_stay_in_screen(True)
        game.show_long_text("There is an Earth Quake! you need to reach the safe zone without getting crushed by the boulders. ",
            DialogLayout.FULL)
        game.show_long_text("you have a flying car, Be Safe", DialogLayout.FULL)
        l2Zeal.set_position(131, 90)
        animation.run_image_animation(l2back,
            [img("""
                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999994444444444499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999445555555555544999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999944555555555555555449999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999455555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999994555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999945555555555555555555555549999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999455555555555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                999999945555555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999c
                                99999945555555555555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999ce
                                9999994555555555555555555555555555499999999999999999999999999999999c99999999999999999999999999999999999999999999cc99999999999999999999999999999999999999999999ce
                                999994555555555555555555555555555554999999999999999999999999999999cec999999999999999999999999999999999999999999cec99999999999999999999999999999999999999999999ce
                                999994555555555555555555555555555554999999999999999999999999999999cec999999999999999999999999999999999999999999cec9999999999999999999999999999999999999999999cee
                                999994555555555555555555555555555554999999999999999999999999999999ceec99999999999999999999999999999999999999999ceec999999999999999999999999999999999999999999cee
                                99999455555555555555c55555555555555499999999999999999999999999999ceeec9999999999999999999999999999999999999999ceeec99999999999999999999999999999999999999999ceee
                                9999945555555555555cec5555555555555499999999999999999999999999999ceeec9999999999999999999999999999999999999999ceeeec9999999999999999999999999999999999999999ceee
                                999994555555555555ceec555555555555549999999999999999999999999999ceeeeec999999999999999999999999999999999999999ceeeec9999999999999999999999999999999999999999ceee
                                99999455555555555ceeeec55555555555549999999999999999999999999999ceeeeec99999999999999999999999999999999999999ceeeeec999999999999999999999999999999999999999ceeee
                                99999455555555555ceeeeec5555555555549999999999999999999999999999ceeeeeec9999999999999999999999999999999999999ceeeeeec99999999999999999999999999999999999999ceeee
                                99999455555555555ceeeeec555555555554999999999999999999999999999ceeeeeeec9999999999999999999999999999999999999ceeeeeec9999999999999999999999999999999999999ceeeee
                                9999945555555555ceeeeeeec55555555554999999999999999999999999999ceeeeeeec999999999999999999999999999999999999ceeeeeeec9999999999999999999999999999999999999ceeeee
                                9999945555555555ceeeeeeec5555555555499999999999999999999999999ceeeeeeeeec99999999999999999999999999999999999ceeeeeeeec999999999999999999999999999999999999ceeeee
                                9999994555555555ceeeeeeeec555555554999999999999999999999999999ceeeeeeeeec99999999999999999999999999999999999ceeeeeeeec99999999999999999999999999999999999ceeeeee
                                999999455555555ceeeeeeeeec555555554999999999999999999999999999ceeeeeeeeeec999999999999999999999999999999999ceeeeeeeeeec9999999999999999999999999999999999ceeeeee
                                999999945555555ceeeeeeeeec55555554999999999999999999999999999ceeeeeeeeeeec999999999999999999999999999999999ceeeeeeeeeec9999999999999999999999999999999999ceeeeee
                                999999945555555ceeeeeeeeeec5555554999999999999999999999999999ceeeeeeeeeeeec99999999999999999999999999999999ceeeeeeeeeec999999999999999999999999999999999ceeeeeee
                                99999999455555ceeeeeeeeeeec555554999999999999999999999999999ceeeeeeeeeeeeec9999999999999999999999999999999ceeeeeeeeeeeec99999999999999999999999999999999ceeeeeee
                                99999999945555ceeeeeeeeeeeec55549999999999999999999999999999ceeeeeeeeeeeeec9999999999999999999999999999999ceeeeeeeeeeeec9999999999999999999999999999999ceeeeeeee
                                99999999994555ceeeeeeeeeeeec55499999999999999999999999999999ceeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeeeeeeec9999999999999999999999999999999ceeeeeeee
                                9999999999944ceeeeeeeeeeeeec4499999999999999999999999999999ceeeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeeeeeeeec999999999999999999999999999999ceeeeeeee
                                9999999999999ceeeeeeeeeeeeeec999999999999999999999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeee
                                999999999999ceeeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeee
                                999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeee
                                999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeee
                                99999999999ceeeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeee
                                99999999999ceeeeeeeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeee
                                99999999999ceeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeee
                                9999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeee
                                9999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeee
                                9999999999ceeeeeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeee
                                999999999ceeeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeee
                                999999999ceeeeeeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeee
                                999999999ceeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeee
                                99999999ceeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeee
                                99999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeee
                                99999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeee
                                9999999ceeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeee
                                9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeee
                                9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeee
                                999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeee
                                999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeee
                                999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeee
                                99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeee
                                99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeee
                                99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeee
                                9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeee
                                9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeee
                                999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeee
                                999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeee
                                ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeee
                                777777777777777777777777777777777777eeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeee
                                7eeee7777ee77777eeee7777eeeee7777777eeeec99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeee
                                7e7777777eee7777e7777777e77777777777eeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeee
                                7ee777777e7e7777eee77777e77777777777eeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeee
                                77eee777eeeee777e7777777eeee77777777eeeeeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999ceeeeeeeeeeeeeeeeeeeeee
                                7777e777e777ee77e7777777e77777777777eeeeeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999ceeeeeeeeeeeeeeeeeeeeee
                                7777e77ee7777e77e7777777e77777777777eeeeeec9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeee
                                eeeee77777777777e7777777eeeee7777777eeeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeee
                                777777777777777777777777777777777777eeeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeeeeeeeeeeeeeeeeeeee
                                7777777777777777777777777777777777771111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                                777eeee77eeeee77ee77e777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                77777ee77e777e77ee77e777e77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                7777ee777e777e77e7e7e777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                777ee7777e777e77e7eee777e77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                777eeee77eeeee77e77ee777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffffbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111f11111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111b
                                bbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111f11111111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111b
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffffffbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbffffffbbbbbbbbbbbbbbbbbbbbbbbffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbfbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffffbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffffbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                """),
                img("""
                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                999999999999999999999999999999999999999999999999999999999999999999cec9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                999999999999999999999999999999999999999999999999999999999999999999cec999999999999999999999999999999999999999999999999999999999999999999999999999999999999cec9999
                                999999999999999999999444444444449999999999999999999999999999999999ceec99999999999999999999999999999999999999999999999999999999999999999999999999999999999cec9999
                                99999999999999999994455555555555449999999999999999999999999999999ceeec99999999999999999999999999999999999999999cec999999999999999999999999999999999999999ceec999
                                999999999999999994455ec555555555554499999999999999999999999999999ceeec99999999999999999999999999999999999999999cec99999999999999999999999999999999999999ceeec999
                                99999999999999994555cec55555555555554999999999999999999999999999ceeeeec9999999999999999999999999999999999999999ceec9999999999999999999999999999999999999ceeec999
                                99999999999999945555ceec5555555555555499999999999999999999999999ceeeeec999999999999999999999999999999999999999ceeec999999999999999999999999999999999999ceeeeec99
                                9999999999999945555ceeec5555555555555549999999999999999999999999ceeeeeec99999999999999999999999999999999999999ceeec999999999999999999999999999999999999ceeeeec99
                                9999999999999455555ceeec555555555555555499999999999999999999999ceeeeeeec9999999999999999999999999999999999999ceeeeec99999999999999999999999999999999999ceeeeeec9
                                999999999999455555ceeeeec55555555555555549999999999999999999999ceeeeeeec9999999999999999999999999999999999999ceeeeec9999999999999999999999999999999999ceeeeeeec9
                                999999999999455555ceeeeec5555555555555554999999999999999999999ceeeeeeeeec999999999999999999999999999999999999ceeeeeec999999999999999999999999999999999ceeeeeeec9
                                999999999994555555ceeeeeec555555555555555499999999999999999999ceeeeeeeeec99999999999999999999999999999999999ceeeeeeec99999999999999999999999999999999ceeeeeeeeec
                                99999999999455555ceeeeeeec555555555555555499999999999999999999ceeeeeeeeeec9999999999999999999999999999999999ceeeeeeec99999999999999999999999999999999ceeeeeeeeec
                                99999999994555555ceeeeeeec55555555555555554999999999999999999ceeeeeeeeeeec999999999999999999999999999999999ceeeeeeeeec9999999999999999999999999999999ceeeeeeeeee
                                9999999999455555ceeeeeeeeec5555555555555554999999999999999999ceeeeeeeeeeeec99999999999999999999999999999999ceeeeeeeeec999999999999999999999999999999ceeeeeeeeeee
                                9999999999455555ceeeeeeeeec555555555555555499999999999999999ceeeeeeeeeeeeec99999999999999999999999999999999ceeeeeeeeeec99999999999999999999999999999ceeeeeeeeeee
                                9999999999455555ceeeeeeeeeec55555555555555499999999999999999ceeeeeeeeeeeeec9999999999999999999999999999999ceeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeee
                                999999999945555ceeeeeeeeeeec55555555555555499999999999999999ceeeeeeeeeeeeeec999999999999999999999999999999ceeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeee
                                999999999945555ceeeeeeeeeeeec555555555555549999999999999999ceeeeeeeeeeeeeeec99999999999999999999999999999ceeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeee
                                99999999994555ceeeeeeeeeeeeec555555555555549999999999999999ceeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeeeeee
                                99999999994555ceeeeeeeeeeeeec55555555555554999999999999999ceeeeeeeeeeeeeeeeec9999999999999999999999999999ceeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeeeee
                                99999999994555ceeeeeeeeeeeeeec5555555555554999999999999999ceeeeeeeeeeeeeeeeec999999999999999999999999999ceeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeee
                                9999999999455ceeeeeeeeeeeeeeec5555555555554999999999999999ceeeeeeeeeeeeeeeeeec99999999999999999999999999ceeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeeeee
                                9999999999455ceeeeeeeeeeeeeeeec55555555555499999999999999ceeeeeeeeeeeeeeeeeeec9999999999999999999999999ceeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeeeee
                                999999999994ceeeeeeeeeeeeeeeeec55555555554999999999999999ceeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeee
                                999999999999ceeeeeeeeeeeeeeeeec5555555555499999999999999ceeeeeeeeeeeeeeeeeeeeec999999999999999999999999ceeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeeeee
                                999999999999ceeeeeeeeeeeeeeeeeec555555554999999999999999ceeeeeeeeeeeeeeeeeeeeec99999999999999999999999ceeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeee
                                99999999999ceeeeeeeeeeeeeeeeeeec555555554999999999999999ceeeeeeeeeeeeeeeeeeeeeec9999999999999999999999ceeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeeeee
                                99999999999ceeeeeeeeeeeeeeeeeeeec5555554999999999999999ceeeeeeeeeeeeeeeeeeeeeeec999999999999999999999ceeeeeeeeeeeeeeeeeeeeec9999999999999999999ceeeeeeeeeeeeeeee
                                9999999999ceeeeeeeeeeeeeeeeeeeeec5555549999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeee
                                9999999999ceeeeeeeeeeeeeeeeeeeeec555549999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999999ceeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeeeee
                                9999999999ceeeeeeeeeeeeeeeeeeeeeec55499999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeee
                                999999999ceeeeeeeeeeeeeeeeeeeeeeec44999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeeeee
                                999999999ceeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999ceeeeeeeeeeeeeeeeee
                                99999999ceeeeeeeeeeeeeeeeeeeeeeeeec999999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeee
                                99999999ceeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeee
                                99999999ceeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeee
                                9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeeeee
                                9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999ceeeeeeeeeeeeeeeeeeee
                                999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeee
                                999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999ceeeeeeeeeeeeeeeeeeeee
                                999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeee
                                99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeeeee
                                99999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeeeee
                                9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999ceeeeeeeeeeeeeeeeeeeeeee
                                9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecc9999ceeeeeeeeeeeeeeeeeeeeeee
                                9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9eeeeeeeeeeeeeeeeeeeeeeeee
                                999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecc999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec999ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99cceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec99ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                9ceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                7777777777777777777777777777777777777eeeeeecceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                77eeee7777ee77777eeee7777eeeee7777777eeeeeeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                77e7777777eee7777e7777777e77777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                77ee777777e7e7777eee77777e77777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                777eee777eeeee777e7777777eeee77777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                77777e777e777ee77e7777777e77777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                77777e77ee7777e77e7777777e77777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                7eeeee77777777777e7777777eeeee7777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                7777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                                7777777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                                7777eeee77eeeee77ee77e777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                777777ee77e777e77ee77e777e77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                77777ee777e777e77e7e7e777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                7777ee7777e777e77e7eee777e77777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                7777eeee77eeeee77e77ee777eeee77777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                7777777777777777777777777777777777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbfffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffbbbbbbbbb
                                bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffffffbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbb111111111111111bbbbbbbbbbbbfbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb11111111f111111bbbbbbbbbbbbbbbbbbbb11111111111111fffffffbbbbbbbbbbbbbb111111111111111b
                                bbbb111111111111111bbbbbbbbbbbbbffbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111fff111bbbbbbbbbbbbbbbbbbbb111111111111111bbbbbbbbbbbbbbbbbbbb111111111111111b
                                bbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbffffffffbbbbbbbbbbbffbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbffffffffffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffff
                                bbbbbbbbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbfffffffffffffffbbbbbbbbbfffffbbbbbbffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbbbbbbbbbbbbbbbbbbbbbbbbbbffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbfffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                """)],
            200,
            True)
        pcm = 1
        selection = 0
    if y == 1:
        p.set_velocity(0, 0)
    if m == 1:
        p2.set_velocity(0, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global Car1, Car2, selection
    if selection == 1:
        game.show_long_text("Press 'A' to Start Game!!", DialogLayout.BOTTOM)
        scene.set_background_image(img("""
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111111
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111
                        9999999999999999999999999999999999999999999999999999999999999999111199999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111
                        9999999999999999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999911111999999999999999999999991111111111111111111111111111
                        9999999999999999999999999999999999999999999999999999999999911111111111111111111999999999999999999999999911111119999999999999999999999111111111111111111111111111
                        9999999999999999999994444444444499999999999999999999911111111111111111111111111199999999999999999999111111111111119999999999999999999999111111111111111111111111
                        9999999999999999994445555555555544499999999999999999111111111111111111111111111119999999999999991111111111111111111111111999999999999999999999111111111111111111
                        9999999999999999945555555555555555549999999999999999111111111111111111111111111111199999999999111111111111111111111111111119999999999999999999999999111111111111
                        9999999999999994455555555555555555554499999999999999111111111111111111111111111111119999999999111111111111111111111111111111119999999999999999999999999999911111
                        9999999999999945555555555555555555555549999999999999111111111111111111111111111111111999999999111111111111111111111111111111111999999999999999999999999999999999
                        9999999999999455555555555555555555555554999999999999111111111111111111111111111111111199999999111111111111111111111111111111111999999999999999999999999999999999
                        9999999999994555555555555555555555555555499999999999111111111111111111111111111111111119999999911111111111111111111111111111111119999999999999999999999999999999
                        9999999999945555555555555555555555555555549999999999111111111111111111111111111111111111999999991111111111111111111111111111111111199999999999999999999999999999
                        9999999999945555555555555555555555555555549999999991111111111111111111111111111111111111199999991111111111111111111111111111111111111999999999999999999999999999
                        9999999999455555555555555555555555555555554999999991111111111111111111111111111111111111119999991111111111111111111111111111111111111999999999999999999999999999
                        9999999994555555555555555555555555555555555499999991111111111111111111111111111111111111119999999111111111111111111111111111111111111999999999999999999999999999
                        9999999994555555555555555555555555555555555499999991111111111111111111111111111111111111119999999111111111111111111111111111111111111999999999999999999999999999
                        9999999994555555555555555555555555555555555499999991111111111111111111111111111111111111119999999111111111111111111111111111111111111999999999999999999999999999
                        9999999945555555555555555555555555555555555549999991111111111111111111111111111111111111119999999111111111111111111111111111111111111999999999999999999999999999
                        9999999945555555555555555555555555555555555549999991111111111111111111111111111111111111119999999999111111111111111111111111111111119999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999911111111111111111111111111111111111199999999999999111111111111111111111111111999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999991111111111111111111111111111111111199999999999999991111111111111111111111199999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999999111111111111111111111111111111111199999999999999999999111111111111111111999999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999999911111111111111111111111111111111199999999999999999999999999991111111119999999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999999999111111111111111111111111111111199999999999999999999999999999911111199999999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999999999999111111111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999999999999999999999999999111111111199999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999945555555555555555555555555555555555549999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999994555555555555555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999994555555555555555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999994555555555555555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999455555555555555555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999945555555555555555555555555555549999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999945555555555555555555555555555549999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999994555555555555555555555555555499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999455555555555555555555555554999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999945555555555555555555555549999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999994455555555555555555554499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999945555555555555555549999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999994445555555555544499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999994444444444449999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        1111111ffffffff11111111ffffffff11111111ffffffff1111111ffffffff11111111ffffffff1111111ffffffff111111111ffffffff11111111ffffffff11111111ffffffff11111111ffffffff11
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        """))
        game.show_long_text("During evening, on mountains tourists who are driving on the mountains, Meet with an accident as the cant see other people who are driving upwards as well as Downwards",
            DialogLayout.FULL)
        Car1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . 6 6 6 6 6 6 6 6 . . . . 
                            . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                            . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                            . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                            . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                            . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                            . 6 8 b b b 8 b b b b 8 6 6 6 6 
                            . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                            . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                            . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                            . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                            . 8 f f f f 8 8 8 8 f f f 8 8 8 
                            . . f f f f f 8 8 f f f f f 8 . 
                            . . . f f f . . . . f f f f . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.entity)
        Car2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . 3 3 3 3 3 3 3 3 . . 
                            . . . . . 3 c 3 3 3 3 3 3 d 3 . 
                            . . . . 3 c c 3 3 3 3 3 3 d c 3 
                            . . d 3 d c c 3 d d d d d d c c 
                            . d 3 3 d c b a a a a a a a 3 c 
                            . 3 3 3 d b a a b b b a b b a 3 
                            . 3 3 3 3 3 a b b b b a b b b a 
                            . 3 3 3 3 a 3 3 3 3 3 a 3 3 3 a 
                            . 3 d d 3 a f a a a f a a a a a 
                            . d d 3 a a a f a a f a a a a a 
                            . a a a a a a a f f f a a a a a 
                            . a a a a f f f a a a a f f f f 
                            . . . a f f f f f a a f f f f f 
                            . . . . f f f f . . . . f f f . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.entity)
        Car1.set_position(7, 95)
        Car1.set_velocity(70, 0)
        Car2.set_position(150, 95)
        Car2.set_velocity(-70, 0)
        selection = 0
    if y == 1:
        p.set_velocity(-20, -8)
    if m == 1:
        p2.set_velocity(30, -10)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global end
    end = 1
sprites.on_overlap(SpriteKind.l2car, SpriteKind.l2safe, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    if fan == 1:
        l2Zeal.set_position(139, 81)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.l2car, on_on_overlap3)

end0 = 0
projectile3: Sprite = None
projectile2: Sprite = None
projectile: Sprite = None
amul: Sprite = None
lol2: Sprite = None
deron2 = 0
Ti = 0
ha2: Sprite = None
lol: Sprite = None
fan = 0
end = 0
p2: Sprite = None
m = 0
pcm = 0
l2shooter3: Sprite = None
l2shooter2: Sprite = None
l2shooter: Sprite = None
l2Zeal: Sprite = None
safe: Sprite = None
l2back: Sprite = None
d = 0
zeal: Sprite = None
yash: Sprite = None
deron: Sprite = None
PSAI: Sprite = None
y = 0
ha: Sprite = None
p: Sprite = None
pavement: Sprite = None
pavement2: Sprite = None
x = 0
Explosion: Sprite = None
Car2: Sprite = None
Car1: Sprite = None
selection = 0
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999999999999999999999999999999999999999999fffffffffff99999999999fffffffffff99999ffffffffff999ffffffffff9999999999999999999999999999999999
        9999999999999999999999999999999fffff9999999f9999999999f9999999999ff999999999ff999999999ff99999999f999999f999999999999f999999999999999999999999999999999999999999
        99999999999999999999999999999ff999999999999f9999999999f999999999f9999999999999f9999999f99999999999f99999f999999999999f999999999999999999999999999999999999999999
        9999999999999999999999999999f99999999999999f9999999999f99999999f999999999999999f99999f9999999999999f9999f999999999999f999999999999999999999999999999999999999999
        999999999999999999999999999f999999999999999f9999999999f99999999f999999999999999f99999f9999999999999f9999f999999999999f999999999999999999999999999999999999999999
        999999999999999999999999999f999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999f999999999999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999f999999999999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999f999999999999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999f999999999999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999ffffffffff999ffffffffff999999999999999999999999999999999
        99999999999999999999999999f9999999999999999ffffffffffff9999999f99999999999999999f999f999999999999999f999999999999f999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999999999999f999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999999999999f999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f9999999f99999999999999999f999f999999999999999f999999999999f999f999999999999999999999999999999999999999999
        99999999999999999999999999f9999999999999999f9999999999f99999999f999999999999999f99999f9999999999999f9999999999999f999f999999999999999999999999999999999999999999
        999999999999999999999999999f999999999999999f9999999999f99999999f999999999999999f99999f9999999999999f9999999999999f999f999999999999999999999999999999999999999999
        999999999999999999999999999f999999999999999f9999999999f999999999f9999999999999f9999999f99999999999f99999999999999f999f999999999999999999999999999999999999999999
        9999999999999999999999999999f99999999999999f9999999999f9999999999ff999999999ff999999999ff99999999f999999999999999f999f999999999999999999999999999999999999999999
        99999999999999999999999999999ff999999999999f9999999999f999999999999fffffffff9999999999999ffffffff9999999ffffffffff999ffffffffff999999999999999999999999999999999
        9999999999999999999999999999999fffff9999999f9999999999f999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999999fffffffff999999999ff999999999f999fffffffff9999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999ff999999999ff9999999ff999999999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999f9999999999999f999999f9f99999999f999f999999999999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999999999999999999999999999999f999999999999999f99999f9f99999999f999f999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999f99999999999999999f9999f99f9999999f999f999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999f99999999999999999f9999f99f9999999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f999f999999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f999f999999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f9999f99999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f9999f99999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f99999f9999f999fffffffff9999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f99999f9999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f999999f999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f999999f999f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999f9999999999999999999f999f9999999f99f999f999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999f99999999999999999f9999f9999999f99f999f999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999f99999999999999999f9999f99999999f9f999f999999999999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999999999999999999999999999999f999999999999999f99999f99999999f9f999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999f9999999999999f999999f999999999ff999f999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999ff999999999ff9999999f999999999ff999f999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999999999999999999999999999fffffffff999999999f9999999999f999fffffffff9999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999ff9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999ffffffff99999999fffffffffff999999999f99f999999999999ffffffffffffff9999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999f9999999f9999999f999999999999999999f9999f999999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        99999999999f999999999999999999999f9999999f9999999f999999999999999999f9999f999999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        99999999999f999999999999999999999f99999999f999999f999999999999999999f9999f999999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        9999999999f9f99999999999999999999f999999999f99999f99999999999999999f999999f99999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        9999999999f9f99999999999999f99999f999999999f99999f99999999999999999f999999f99999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        999999999f999f9999999999999999999f99999999f999999f99999999999999999f999999f99999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        999999999f999f9999999999999999999f9999999f9999999f99999999999999999f999999f99999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        99999999f99999f999999999999999999ffffffff99999999f9999999999999999fffffffff99999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        99999999f99999f999999999999999999f999999999999999fffffffffff999999f99999999f9999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        9999999fffffffff99999999999999999f9999999999999999999999999f999999f99999999f9999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        9999999f9999999f99999999999999999f9999999999999999999999999f99999f9999999999f999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        999999f999999999f9999999999999999f9999999999999999999999999f99999f9999999999f999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        999999f999999999f9999999999999999f9999999999999999999999999f99999f9999999999f999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        99999f99999999999f999999999999999f9999999999999999999999999f99999f9999999999f999999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        99999f99999999999f999999999999999f9999999999999999999999999f9999f999999999999f99999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        9999f9999999999999f99999999999999f9999999999999999999999999f9999f999999999999f99999999999999f9999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999f99999f999999999999f99fffffffffff99f9f999999999999f99f9999ffffffffffffff9999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999f999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        999999999999999999999999999999999f999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        99fffffffffffff9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        99f99999999999ff9999999999999999f9999999999f9fffffff9fffffffff9fffffff99999fffffff99999fffff9999999999999999ffffffff9f9999999999f999999ff9999999fffffff9f99999f9
        99f999999999999ff999999999999999ff99999999ff9f99999999999f99999f999999999ff9999999ff999f9999f999999999999999f99999999ff99999999ff999999ff9999999f9999999f99999f9
        99f9999999999999f999999999999999f9f999999f9f9f99999999999f99999f99999999f99999999999f99f99999f99999999999999f99999999f9ff9999ff9f999999ff9999999f9999999f99999f9
        99f9999999999999ff99999999999999f99f9999f99f9f99999999999f99999f99999999f99999999999f99f999999f9999999999999f99999999f999f99f999f99999f99f999999f9999999f99999f9
        99f99999999999999f9999999999f999f99f9999f99f9f99999999999f99999f9999999f9999999999999f9f999999f9999999999999f99999999f9999ff9999f99999f99f999999f9999999f99999f9
        99f99999999999999f99999999999999f999f99f999f9f99999999999f99999f9999999f9999999999999f9f999999f9999999999999f99999999f9999999999f99999f99f999999f9999999f99999f9
        99f9999999999999f999999999999999f9999ff9999f9f99999999999f99999f9999999f9999999999999f9f99999f99999999999999f99999999f9999999999f9999f9999f99999f9999999f99999f9
        99f999999999999ff999999999999999f9999999999f9f99999999999f99999f9999999f9999999999999f9ffffff999999999999999f99999999f9999999999f9999f9999f99999f9999999f99999f9
        99f99999999999ff9999999999999999f9999999999f9fffffff99999f99999fffffff9f9999999999999f9ff9999999999999999999fffffff99f9999999999f9999f9999f99999fffffff9fffffff9
        99f999999999fff99999999999999999f9999999999f9f99999999999f99999f9999999f9999999999999f9f9f999999999999999999999999f99f9999999999f9999ffffff99999999999f9f99999f9
        99fffffffffff9999999999999999999f9999999999f9f99999999999f99999f9999999f9999999999999f9f9f999999999999999999999999f99f9999999999f999f999999f9999999999f9f99999f9
        99f999999999fff99999999999999999f9999999999f9f99999999999f99999f99999999f99999999999f99f99f99999999999999999999999f99f9999999999f999f999999f9999999999f9f99999f9
        99f999999999999f9999999999999999f9999999999f9f99999999999f99999f99999999f99999999999f99f999f9999999999999999999999f99f9999999999f999f999999f9999999999f9f99999f9
        99f999999999999ff999999999999999f9999999999f9f99999999999f99999f999999999ff9999999ff999f9999f999999999999999999999f99f9999999999f99f99999999f999999999f9f99999f9
        99f9999999999999f999999999999999f9999999999f9f99999999999f99999f99999999999fffffff99999f99999f99999999999999999999f99f9999999999f99f99999999f999999999f9f99999f9
        99f9999999999999f999999999999999f9999999999f9f99999999999f99999f99999999999999999999999f99999f99999999999999999999f99f9999999999f99f99999999f999999999f9f99999f9
        99f999999999999ff99999999999f999f9999999999f9f99999999999f99999f99999999999999999999999f999999f999999999999ffffffff99f9999999999f9f9999999999f99fffffff9f99999f9
        99f999999999999f9999999999999999f9999999999f9fffffff99999f99999fffffff99999999999999999f9999999f9999999999999999999999999999999999999999999999999999999999999999
        99f99999999999ff999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        99f9999999999f99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        99fffffffffff999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
"""))
selection = 1

def on_forever():
    global lol, ha2, Ti, deron2, p2, m
    if d == 1:
        if deron.overlaps_with(ha):
            sprites.destroy(PSAI)
            lol = sprites.create(img("""
                    f f f f f f f f f f f f f f f f 
                                    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
                                    f 2 f f f f 2 2 2 f f f f f 2 f 
                                    f 2 f 2 2 2 2 2 2 2 2 f 2 2 2 f 
                                    f 2 f f f f 2 2 2 2 2 f 2 2 2 f 
                                    f 2 2 2 2 f 2 2 2 2 2 f 2 2 2 f 
                                    f 2 f f f f 2 2 2 2 2 f 2 2 2 f 
                                    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
                                    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
                                    f 2 f f f f 2 2 2 f f f f f 2 f 
                                    f 2 f 2 2 f 2 2 2 f 2 2 2 f 2 f 
                                    f 2 f 2 2 f 2 2 2 f f f f f 2 f 
                                    f 2 f 2 2 f 2 2 2 f 2 2 2 2 2 f 
                                    f 2 f f f f 2 2 2 f 2 2 2 2 2 f 
                                    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
                                    f f f f f f f f f f f f f f f f
                """),
                SpriteKind.player)
            lol.set_position(24, 63)
        if yash.overlaps_with(ha):
            sprites.destroy(ha)
            ha2 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . 6 6 6 6 6 6 6 6 . . . . 
                                    . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                                    . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                                    . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                                    . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                                    . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                                    . 6 8 b b b 8 b b b b 8 6 6 6 6 
                                    . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                                    . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                                    . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                                    . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                                    . 8 f f f f 8 8 8 8 f f f 8 8 8 
                                    . . f f f f f 8 8 f f f f f 8 . 
                                    . . . f f f . . . . f f f f . . 
                                    . . . . . . . . . . . . . . . .
                """),
                SpriteKind.player)
            ha2.set_position(50, 66)
            ha2.set_velocity(30, 12)
            Ti = 1
            deron2 = 1
        if yash.overlaps_with(p):
            sprites.destroy(p)
            p2 = sprites.create(img("""
                    . . . . e e e e e . . . . . . . 
                                    . . . e 2 2 2 2 2 e e . . . . . 
                                    . . e 2 2 2 2 2 2 2 e e . . . . 
                                    . e b 4 2 2 2 4 4 4 9 e . . . . 
                                    e b 9 4 2 2 4 4 4 4 9 9 e e . . 
                                    e 9 9 4 2 4 4 4 4 4 9 9 2 2 e . 
                                    e 9 9 2 4 4 4 4 4 2 9 9 2 2 2 e 
                                    e 9 9 e e e e e e e 9 9 2 2 2 e 
                                    e 9 b e b e b b b e b 9 2 2 2 e 
                                    e b e b b e b b b b e e e e 2 e 
                                    e e e 2 2 e 2 2 2 2 e e 3 3 e e 
                                    e e e e e e e e e e e e e 3 3 e 
                                    e e e e e e e e e e e e e e e e 
                                    e e f f f e e e e f f f e e e e 
                                    . f b f f f e e f b f f f e e . 
                                    . . b b c . . . . b b c . . . .
                """),
                SpriteKind.player)
            p2.set_position(44, 62)
            p2.set_velocity(30, -10)
            m = 1
forever(on_forever)

def on_forever2():
    global lol2, deron2, amul
    if deron2 == 1:
        if p.overlaps_with(pavement):
            sprites.destroy(lol)
            lol2 = sprites.create(img("""
                    f f f f f f f f f f f f f f f f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 f f f f 7 7 7 f f f f f 7 f 
                                    f 7 f 7 7 7 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 7 7 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 f f 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 7 f 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f f f f 7 7 7 f f f f f 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f f f f f f f f f f f f f f f f
                """),
                SpriteKind.player)
            lol2.set_position(24, 63)
            deron2 = 0
        elif p.overlaps_with(pavement2):
            sprites.destroy(lol)
            lol2 = sprites.create(img("""
                    f f f f f f f f f f f f f f f f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 f f f f 7 7 7 f f f f f 7 f 
                                    f 7 f 7 7 7 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 7 7 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 f f 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 7 f 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f f f f 7 7 7 f f f f f 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f f f f f f f f f f f f f f f f
                """),
                SpriteKind.player)
            lol2.set_position(24, 63)
            deron2 = 0
        elif p.overlaps_with(zeal):
            sprites.destroy(lol)
            lol2 = sprites.create(img("""
                    f f f f f f f f f f f f f f f f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 f f f f 7 7 7 f f f f f 7 f 
                                    f 7 f 7 7 7 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 7 7 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 f f 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f 7 7 f 7 7 7 f 7 7 7 f 7 f 
                                    f 7 f f f f 7 7 7 f f f f f 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f 
                                    f f f f f f f f f f f f f f f f
                """),
                SpriteKind.player)
            lol2.set_position(24, 63)
            deron2 = 0
        else:
            amul = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . 4 4 4 4 4 . . . . . . 
                                    . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                                    . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                                    . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                                    . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                                    . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                                    . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                                    . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                    . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                    . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                                    . . . 2 2 4 d 5 5 d d 4 4 . . . 
                                    . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                                    . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                                    . . . . . 2 2 2 2 2 2 . . . . .
                """),
                SpriteKind.entity)
            amul.set_position(p.x, p.y)
            sprites.destroy(ha2)
            sprites.destroy(p)
            animation.run_image_animation(amul,
                [img("""
                        . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . . 4 4 4 4 4 . . . . . . 
                                        . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                                        . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                                        . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                                        . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                                        . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                                        . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                                        . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                        . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                        . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                                        . . . 2 2 4 d 5 5 d d 4 4 . . . 
                                        . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                                        . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                                        . . . . . 2 2 2 2 2 2 . . . . .
                    """),
                    img("""
                        . . . . 2 2 2 2 2 2 2 2 . . . . 
                                        . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                                        . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                                        . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                                        . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                                        2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                                        2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                                        4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                                        . . b b b b 2 4 4 2 b b b b . . 
                                        . b d d d d 2 4 4 2 d d d d b . 
                                        b d d b b b 2 4 4 2 b b b d d b 
                                        b d d b b b b b b b b b b d d b 
                                        b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                                        . . b b d d 1 1 3 d d 1 b b . . 
                                        . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                                        . . . 2 2 4 4 4 4 4 2 2 2 . . .
                    """),
                    img("""
                        . . . . . . . . b b . . . . . . 
                                        . . . . . . . . b b . . . . . . 
                                        . . . b b b . . . . . . . . . . 
                                        . . b d d b . . . . . . . b b . 
                                        . b d d d b . . . . . . b d d b 
                                        . b d d b . . . . b b . b d d b 
                                        . b b b . . . . . b b . . b b . 
                                        . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . 
                                        . . b b b d d d d d d b b b . . 
                                        . b d c c c b b b b c c d d b . 
                                        b d d c b . . . . . b c c d d b 
                                        c d d b b . . . . . . b c d d c 
                                        c b d d d b b . . . . b d d c c 
                                        . c c b d d d d b . c c c c c c 
                                        . . . c c c c c c . . . . . . .
                    """)],
                100,
                False)
            pause(200)
            sprites.destroy(amul, effects.fire, 500)
forever(on_forever2)

def on_forever3():
    global projectile, projectile2, projectile3, fan, pcm, end0
    if pcm == 1:
        for index in range(10000):
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . . 
                                    . . c c b b b a c a a a c . . . 
                                    . c c a b a c b a a a b c c . . 
                                    . c a b c f f f b a b b b a . . 
                                    . c a c f f f 8 a b b b b b a . 
                                    . c a 8 f f 8 c a b b b b b a . 
                                    c c c a c c c c a b c f a b c c 
                                    c c a a a c c c a c f f c b b a 
                                    c c a b 6 a c c a f f c c b b a 
                                    c a b c 8 6 c c a a a b b c b c 
                                    c a c f f a c c a f a c c c b . 
                                    c a 8 f c c b a f f c b c c c . 
                                    . c b c c c c b f c a b b a c . 
                                    . . a b b b b b b b b b b b c . 
                                    . . . c c c c b b b b b c c . . 
                                    . . . . . . . . c b b c . . . .
                """),
                l2shooter,
                0,
                50)
            projectile2 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . . 
                                    . . c c b b b a c a a a c . . . 
                                    . c c a b a c b a a a b c c . . 
                                    . c a b c f f f b a b b b a . . 
                                    . c a c f f f 8 a b b b b b a . 
                                    . c a 8 f f 8 c a b b b b b a . 
                                    c c c a c c c c a b c f a b c c 
                                    c c a a a c c c a c f f c b b a 
                                    c c a b 6 a c c a f f c c b b a 
                                    c a b c 8 6 c c a a a b b c b c 
                                    c a c f f a c c a f a c c c b . 
                                    c a 8 f c c b a f f c b c c c . 
                                    . c b c c c c b f c a b b a c . 
                                    . . a b b b b b b b b b b b c . 
                                    . . . c c c c b b b b b c c . . 
                                    . . . . . . . . c b b c . . . .
                """),
                l2shooter2,
                0,
                50)
            projectile3 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . . 
                                    . . c c b b b a c a a a c . . . 
                                    . c c a b a c b a a a b c c . . 
                                    . c a b c f f f b a b b b a . . 
                                    . c a c f f f 8 a b b b b b a . 
                                    . c a 8 f f 8 c a b b b b b a . 
                                    c c c a c c c c a b c f a b c c 
                                    c c a a a c c c a c f f c b b a 
                                    c c a b 6 a c c a f f c c b b a 
                                    c a b c 8 6 c c a a a b b c b c 
                                    c a c f f a c c a f a c c c b . 
                                    c a 8 f c c b a f f c b c c c . 
                                    . c b c c c c b f c a b b a c . 
                                    . . a b b b b b b b b b b b c . 
                                    . . . c c c c b b b b b c c . . 
                                    . . . . . . . . c b b c . . . .
                """),
                l2shooter3,
                0,
                50)
            pause(1000)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . . 
                                    . . c c b b b a c a a a c . . . 
                                    . c c a b a c b a a a b c c . . 
                                    . c a b c f f f b a b b b a . . 
                                    . c a c f f f 8 a b b b b b a . 
                                    . c a 8 f f 8 c a b b b b b a . 
                                    c c c a c c c c a b c f a b c c 
                                    c c a a a c c c a c f f c b b a 
                                    c c a b 6 a c c a f f c c b b a 
                                    c a b c 8 6 c c a a a b b c b c 
                                    c a c f f a c c a f a c c c b . 
                                    c a 8 f c c b a f f c b c c c . 
                                    . c b c c c c b f c a b b a c . 
                                    . . a b b b b b b b b b b b c . 
                                    . . . c c c c b b b b b c c . . 
                                    . . . . . . . . c b b c . . . .
                """),
                l2shooter,
                0,
                50)
            projectile2 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . . 
                                    . . c c b b b a c a a a c . . . 
                                    . c c a b a c b a a a b c c . . 
                                    . c a b c f f f b a b b b a . . 
                                    . c a c f f f 8 a b b b b b a . 
                                    . c a 8 f f 8 c a b b b b b a . 
                                    c c c a c c c c a b c f a b c c 
                                    c c a a a c c c a c f f c b b a 
                                    c c a b 6 a c c a f f c c b b a 
                                    c a b c 8 6 c c a a a b b c b c 
                                    c a c f f a c c a f a c c c b . 
                                    c a 8 f c c b a f f c b c c c . 
                                    . c b c c c c b f c a b b a c . 
                                    . . a b b b b b b b b b b b c . 
                                    . . . c c c c b b b b b c c . . 
                                    . . . . . . . . c b b c . . . .
                """),
                l2shooter,
                0,
                50)
            projectile3 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . c c c a c . . . . 
                                    . . c c b b b a c a a a c . . . 
                                    . c c a b a c b a a a b c c . . 
                                    . c a b c f f f b a b b b a . . 
                                    . c a c f f f 8 a b b b b b a . 
                                    . c a 8 f f 8 c a b b b b b a . 
                                    c c c a c c c c a b c f a b c c 
                                    c c a a a c c c a c f f c b b a 
                                    c c a b 6 a c c a f f c c b b a 
                                    c a b c 8 6 c c a a a b b c b c 
                                    c a c f f a c c a f a c c c b . 
                                    c a 8 f c c b a f f c b c c c . 
                                    . c b c c c c b f c a b b a c . 
                                    . . a b b b b b b b b b b b c . 
                                    . . . c c c c b b b b b c c . . 
                                    . . . . . . . . c b b c . . . .
                """),
                l2shooter3,
                0,
                50)
            fan = 1
        pcm = 0
        end0 = 1
forever(on_forever3)

def on_forever4():
    if Ti == 1:
        if zeal.overlaps_with(ha2):
            ha2.set_velocity(50, 0)
forever(on_forever4)

def on_forever5():
    global end
    if m == 1:
        if d == 1:
            if p2.overlaps_with(deron):
                end = 1
forever(on_forever5)

def on_forever6():
    if end == 1:
        sprites.destroy_all_sprites_of_kind(SpriteKind.l2sprites)
        sprites.destroy_all_sprites_of_kind(SpriteKind.l2car)
        sprites.destroy_all_sprites_of_kind(SpriteKind.l2safe)
        sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        sprites.destroy_all_sprites_of_kind(SpriteKind.pave)
        game.show_long_text("Yay ! you won the game!", DialogLayout.BOTTOM)
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffff1111ffff1111111111fffffffff1111111111111111fff11111111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffff11ffffffff1fffffffff1ffffffff1ffffffffffffffffff1ffffffffff1fffffffffff11111111111111111111fffff11111111111111111fffff111111111111111fffffffffffff
                        fffffffffffff1ffffffffff1ffffffffff1fffffff1ffffffffffffffffff1fffffffffff1fffffffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffffff1fffffffffff1fffffffffff1ffffff1ffffffffffffffffff1ffffffffffff1ffffffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        fffffffffff1ffffffffffff1ffffffffffff1fffff1ffffffffffffffffff1fffffffffffff1fffffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        fffffffffff1ffffffffffff1fffffffffffff1ffff1ffffffffffffffffff1ffffffffffffff1ffffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffff1fffffffffffff1ffffffffffff1fffff1ffffffffffffffffff1fffffffffffffff1fffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffff1fffffffffffff1ffffffffffff1fffff1ffffffffffffffffff1ffffffffffffffff1ffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffff1fffffffffffff1fffffffffff1ffffff1ffffffffffffffffff1ffffffffffffffff1ffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffff1fffffffffffff111111111111fffffff1ffffffffffffffffff1ffffffffffffffff1ffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffff1fffffffffffff11fffffffffffffffff1111111111111111fff1ffffffffffffffff1ffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffff1fffffffffffff1f1ffffffffffffffff1ffffffffffffffffff1ffffffffffffffff1ffffffffffffff1fffffffffffffffffffffff1fffffffffffff1fffffffffffffffffffffffffff
                        ffffffffff1fffffffffffff1ff1fffffffffffffff1ffffffffffffffffff1ffffffffffffffff1ffffffffffffff1fffffffffffffffffffffff1fffffffffffff11111111111111ffffffffffffff
                        ffffffffff1fffffffffffff1fff1ffffffffffffff1ffffffffffffffffff1ffffffffffffffff1ffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        ffffffffff1fffffffffffff1ffff1fffffffffffff1ffffffffffffffffff1fffffffffffffff1fffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        fffffffffff1ffffffffffff1fffff1ffffffffffff1ffffffffffffffffff1ffffffffffffff1ffffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        fffffffffff1ffffffffffff1ffffff1fffffffffff1ffffffffffffffffff1fffffffffffff1fffffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        ffffffffffff1fffffffffff1fffffff1ffffffffff1ffffffffffffffffff1ffffffffffff1ffffffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        fffffffffffff1ffffffffff1ffffffff1fffffffff1ffffffffffffffffff1fffffffffff1fffffffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        ffffffffffffff11ffffffff1fffffffff1ffffffff1ffffffffffffffffff1ffffffffff1ffffffffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        ffffffffffffffff1111ffff1ffffffffff1fffffff1111111111111111fff11111111111fffffffffffffffffffff1fffffffffffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111111111111111ffffffffffffff1ffffffffffffffffffffffffff1ffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111111111ffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffffffff1ff11111ffffff1fffffffff1ff111111111ffff11ffffff1fffffffff1fff1111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffffffff1ff1ffff1fffff1fffffffff1ffffff1ffffffff11ffffff1fffffffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffffffff1ff1fffff1ffff1fffffffff1ffffff1ffffffff11ffffff11ffffffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffff1fffffff1fff1ffffff1fff1fffffffff1ffffff1ffffffff11ffffff1f1fffffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffff1fffffff1fff1ffffff1fff1fffffffff1ffffff1fffffff1ff1fffff1f1fffffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffff1fffffff1fff1ffffff1fff1fffffffff1ffffff1fffffff1ff1fffff1ff1ffffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffff1fffff1ffff1fffff1ffff1fffffffff1ffffff1fffffff1ff1fffff1fff1fffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffff1fffff1ffff1ffff1fffff1fffffffff1ffffff1fffffff1ff1fffff1fff1fffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1fff1fffff11111ffffff1fffffffff1ffffff1ffffff111111ffff1ffff1ffff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1fff1fffff11fffffffff1fffffffff1ffffff1ffffff1ffff1ffff1fffff1fff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1fff1fffff1f1ffffffff1fffffffff1ffffff1ffffff1ffff1ffff1fffff1fff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffff1f1ffffff1ff1fffffff1fffffffff1ffffff1fffff1ffffff1fff1ffffff1ff1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffff1f1ffffff1fff11ffffff1fffffff1fffffff1fffff1ffffff1fff1fffffff1f1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffff1f1ffffff1fffff1ffffff1fffff1ffffffff1fffff1ffffff1fff1fffffff1f1ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffff1fffffff1ffffff1ffffff11111fffffffff1ffff1ffffffff1ff1ffffffff11ffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff111111fffffff11111111fff11111fffffffff1111111fffff1fffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffff1ffffff1ffffffffff1ffff1fffffff1fffffff1ffff1fffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffff1fffff1ffffffffff1fffff1fffff1fffffffff1fff11ffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffffff1ffff1ffffffffff1ffffff1fff1fffffffffff1ff1f1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffffff1fff1ffffffffff1ffffff1fff1fffffffffff1ff1f1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffffff1fff1ffffffffff1ffffff1fff1fffffffffff1ff1ff1ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffffff1fff11111111fff1fffff1ffff1fffffffffff1ff1ff1ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffffff1fff1ffffffffff1ffff1fffff1fffffffffff1ff1fff1fff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffffff1fff1ffffffffff11111ffffff1fffffffffff1ff1ffff1ff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffffff1fff1ffffffffff11fffffffff1fffffffffff1ff1ffff1ff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffffff1ffff1ffffffffff1f1fffffffff1fffffffff1fff1fffff1f1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1ffffff1fffff1ffffffffff1ff11ffffffff1fffffff1ffff1ffffff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffff1ffffff1ffffffffff1ffff1ffffffff1111111fffff1ffffff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff111111fffffff11111111fff1fffff1fffffffffffffffffff1fffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1111111111fff11111111ffffff11fffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffff1fff1fffffffffffff11fffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffff1ffff1ffffffffffff1ff1ffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffff1fffff1ffffffffffff1ff1ffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffff1fffff1ffffffffffff1ff1ffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffff1ffffff1fffffffffff1ffff1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffff1fffffff11111111ffff1ffff1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffff1ffffffff1ffffffffff11111111ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1fffffffff1ffffffffff1ffffff1ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1fffffffff1ffffffffff1ffffff1ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffff1ffffffffff1fffffffff1ffffffff1fff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffff1fffffffffff1fffffffff1ffffffff1fff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1111111111fff11111111f1ffffffffff1ff11111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fff1fffffff1ffffffff11111111ff1fffff1ff1fffffff1f1111111111ff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffff1fff11ffff1fffffffff1fffff1ff1fffffff1fffff1fffffff1ffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffff1fffff1fff11ffff1fffffffff1fffff1ff1fffffff1fffff1fffffff1fffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffff1fff1ffff11ffff1fffffffff1fffff1fff1fffff1ffffff1fffffff1fffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffff1f1ffff1ff1fff1fffffffff1fffff1fff1fffff1ffffff1fffffff1fffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffff1f1ffff1ff1fff11111111ff1111111ffff1fff1fffffff1fffffff1fffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1fffff1ff1ffffffffff1ff1fffff1ffff1fff1fffffff1fffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1ffff111111fffffffff1ff1fffff1ffff1fff1fffffff1fffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1ffff1ffff1fffffffff1ff1fffff1fffff1f1ffffffff1fffffff1ff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1ffff1ffff1fffffffff1ff1fffff1fffff1f1ffffffff1fffffff1fff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffff1fff1ffffff1f11111111ff1fffff1ffffff1fffff1111111111ff1fffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
forever(on_forever6)
