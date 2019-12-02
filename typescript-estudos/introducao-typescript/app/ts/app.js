// HELLO WORLD
var world = "World";
console.log("Hello, " + world);
var number10 = 10;
console.log(number10); // saida: 10
// POSSIBILIDADE DE TIPOS INDEFINIDOS OU TIPOS IMPLÍCITOS
var indefinido;
console.log(indefinido); // saida: undefined
console.log(typeof (indefinido)); // saida: undefined
var variavel1 = 10; // sem usar tipagem, o primeiro tipo atribuido vai ser considerado o tipo da variável
// variavel1 = "texto texto texto" // não compila
console.log(typeof (variavel1)); // saida: number
var variavel2 = "texto texto texto"; // o mesmo que não declarar o tipo explicitamente é usar o any
console.log(variavel2); // saida: texto texto texto
console.log(typeof (variavel2)); // saida: string
// ESTUDO DOS TIPOS EXPLÍCITOS
var isAdmin = true;
console.log(typeof (isAdmin)); // saida: boolean
console.log(isAdmin); // saida: true
isAdmin = false;
console.log(isAdmin); // saida: false
var inteiro = 6;
console.log(typeof (inteiro)); // saida: number
console.log(inteiro); // saida: 6
var real = 4.8;
console.log(typeof (real)); // saida: number
console.log(real); // saida: 4.8
var hex = 0xf0a0d;
console.log(typeof (hex)); // saida: number
console.log(hex); // saida: 985613
var binario = 42;
console.log(typeof (binario)); // saida: number
console.log(binario); // saida: 42
var octal = 228;
console.log(typeof (octal)); // saida: number
console.log(octal); // saida: 228
var texto = "texto texto texto";
console.log(typeof (texto));
console.log(texto);
var nome = "Felipe Gabriel";
var idade = 19;
var frase = "Meu nome \u00E9 " + nome + ".\nCompletarei " + (idade + 1) + " anos ano que vem."; // frase feita com crases sai igual a como está no código
console.log(frase);
var Cores;
(function (Cores) {
    Cores[Cores["Vermelho"] = 0] = "Vermelho";
    Cores[Cores["Verde"] = 1] = "Verde";
    Cores[Cores["Azul"] = 2] = "Azul";
})(Cores || (Cores = {}));
;
console.log("Cores.Verde: " + Cores.Verde);
console.log("Cores[2]: " + Cores[2]);
var numeros1 = [1, 2, 3];
console.log(typeof (numeros1));
var numeros2 = [6, 5, 4];
console.log(typeof (numeros2));
numeros1.push(numeros2.pop());
console.log(numeros1);
console.log(numeros2);
console.log(numeros1 + "," + numeros2.reverse());
var cidade = "Teresina";
var altura = 75.233333;
console.log("Cidade: " + cidade.concat(" - THE"));
console.log("Altura: " + altura.toFixed(2));
// ESTRUTURAS DE CONDIÇÃO E REPETIÇÃO
for (var i_1 = 0; i_1 < 3; i_1++) {
    console.log(i_1); // 0, 1, 2
    console.log(typeof (i_1)); // number
}
for (var i = 0; i < 3; i++) {
    console.log(i); // 0, 1, 2
}
console.log(i); // 3
var idade_votando = 17;
if (idade >= 16 && idade_votando < 18) {
    console.log("voto facultativo");
}
var expressao = 2;
switch (expressao) {
    case 1:
        console.log("Valor 1");
        break;
    case 2:
        console.log("Valor 2");
        break;
    default:
        console.log("Outro valor");
        break;
}
;
var numero = 100;
numero++;
numero--;
numero += 2;
numero -= 1;
numero *= 4;
numero /= 2;
console.log(numero); // 202
var contador = 1;
console.log("\nitera\u00E7\u00E3o 1: ");
while (contador <= 3) {
    console.log(contador);
    contador++;
}
var numeros3 = [4, 5, 6];
console.log("\nitera\u00E7\u00E3o 2: ");
for (var i_2 = 0; i_2 < numeros3.length; i_2++) {
    numeros3[i_2] = numeros3[i_2] * 2;
    console.log(numeros3[i_2]);
}
var numeros4 = [4, 5, 6];
//faz a iteração pelos elementos
console.log("\nitera\u00E7\u00E3o 3: ");
for (var _i = 0, numeros4_1 = numeros4; _i < numeros4_1.length; _i++) {
    var numero_1 = numeros4_1[_i];
    console.log(numero_1); // 4, 5, 6
}
//faz a iteração pelos índices
console.log("\nitera\u00E7\u00E3o 4: ");
for (var numero_index in numeros4) {
    console.log("\nindice: " + numero_index); // 0, 1, 2
    console.log("n\u00FAmero: " + numeros4[numero_index]); // 4, 5, 6
}
function add1(x, y) {
    return x + y;
}
console.log(add1(2, 3));
var variavel_add = function add2(x, y) {
    return x + y;
};
console.log(variavel_add(2, 4));
function nomeCompleto(nome, sobrenome) {
    if (sobrenome === void 0) { sobrenome = "Silva"; }
    return nome + " " + sobrenome;
}
console.log(nomeCompleto('Felipe', 'Gabriel')); // Felipe Gabriel
console.log(nomeCompleto('Felipe')); // Felipe Silva
function somar() {
    var numeros = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        numeros[_i] = arguments[_i];
    }
    var soma = 0;
    for (var _a = 0, numeros_1 = numeros; _a < numeros_1.length; _a++) {
        var numero_2 = numeros_1[_a];
        soma += numero_2;
    }
    return soma;
}
console.log(somar()); // 0
console.log(somar(1, 2)); // 3
console.log(somar(1, 2, 3)); // 6 
function dobra1(x) {
    return 2 * x;
}
console.log(dobra1(5)); //10
var dobra2 = function (x) { return 2 * x; };
console.log(dobra2(2)); //4
var numeros5 = [1, 2, 3, 4];
numeros5 = numeros5.map(function (x) { return 2 * x; });
console.log(numeros5); //[2,4,6,8]
//# sourceMappingURL=app.js.map