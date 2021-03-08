# Return-of-the-bowling
Este programa es una calculadora de partidas de bolos. El programa no es capaz de calcular partidas sobre la marcha de una partida, le ahs de pasar una ficha de puntuación completa. Una partida de bolos tiene 10 turnos, y hasta 2 tiradas por turno (excepto en el último que hay hasta 3). 
En el caso de que consigas hacer un pleno (tirar los 10 bolos, representado con una X) el turno se acaba, sumarás 10 puntos y las siguientes 2 tiradas se sumarán también a ese turno, así que si haces un pleno y luego haces 2 tiradas, una de 5 bolos y otra de 2, en total sumarías 17 puntos en el turno del pleno y 7 del segundo turno (24 puntos). 

Si haces un semi-pleno (tirar los 10 bolos en 2 tiradas en el mismo turno, se representa con /) Se aplica la misma norma que con el pleno, pero solo con la proxima tirada, en el caso anterior el turno del semi-pleno sumaría 15 puntos y el segundo turno 7 (22 en total).

Los puntos nulos (no tirar ningun bolo, se representa con -) no suman puntuación y cuentan para la acumulación de tiradas de los plenos y semi-plenos.

En el último turno, tendrás una tercera tirada en caso de que consigas hacer o un pleno o un semipleno en ese turno. Además, la norma de acumulación de turnos en los plenos y semi-plenos no se aplica en el último turno, asi que si consigues hacer 3 plenos en el último turno solo serían 30 puntos.

Esta vez he hecho el programa de una forma más eficiente y con menos code smells.
