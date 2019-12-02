// HELLO WORLD

let world : string = "World";
console.log("Hello, " + world);

let number10 : number = 10;
console.log(number10); // saida: 10

// POSSIBILIDADE DE TIPOS INDEFINIDOS OU TIPOS IMPLÍCITOS

let indefinido;
console.log(indefinido); // saida: undefined
console.log(typeof(indefinido)); // saida: undefined

let variavel1 = 10; // sem usar tipagem, o primeiro tipo atribuido vai ser considerado o tipo da variável
// variavel1 = "texto texto texto" // não compila
console.log(typeof(variavel1)); // saida: number

let variavel2 : any = "texto texto texto"; // o mesmo que não declarar o tipo explicitamente é usar o any
console.log(variavel2); // saida: texto texto texto
console.log(typeof(variavel2)); // saida: string

// ESTUDO DOS TIPOS EXPLÍCITOS

let isAdmin : boolean = true;
console.log(typeof(isAdmin)); // saida: boolean
console.log(isAdmin); // saida: true
isAdmin = false;
console.log(isAdmin); // saida: false

let inteiro : number = 6;
console.log(typeof(inteiro)); // saida: number
console.log(inteiro); // saida: 6

let real : number = 4.8;
console.log(typeof(real)); // saida: number
console.log(real); // saida: 4.8

let hex: number = 0xf0a0d;
console.log(typeof(hex)); // saida: number
console.log(hex); // saida: 985613

let binario: number = 0b101010;
console.log(typeof(binario)); // saida: number
console.log(binario); // saida: 42

let octal: number = 0o344;
console.log(typeof(octal)); // saida: number
console.log(octal); // saida: 228

let texto : string = "texto texto texto";
console.log(typeof(texto));
console.log(texto);

let nome : string = "Felipe Gabriel";
let idade : number = 19;
let frase : string = `Meu nome é ${nome}.
Completarei ${idade + 1} anos ano que vem.`; // frase feita com crases sai igual a como está no código
console.log(frase);

enum Cores {Vermelho, Verde, Azul};
console.log(`Cores.Verde: ${Cores.Verde}`);
console.log(`Cores[2]: ${Cores[2]}`);

let numeros1 : number[] = [1, 2, 3];
console.log(typeof(numeros1));

let numeros2 : Array<number> = [6, 5, 4];
console.log(typeof(numeros2));

numeros1.push(numeros2.pop());
console.log(numeros1);
console.log(numeros2);
console.log(`${numeros1},${numeros2.reverse()}`);

let cidade : string = "Teresina";
let altura : number = 75.233333;

console.log(`Cidade: ${cidade.concat(" - THE")}`);
console.log(`Altura: ${altura.toFixed(2)}`);

// ESTRUTURAS DE CONDIÇÃO E REPETIÇÃO

for (let i : number = 0; i < 3; i++) {
    console.log(i); // 0, 1, 2
    console.log(typeof(i)); // number
}

for (var i : number = 0; i < 3; i++) {
    console.log(i); // 0, 1, 2
}
console.log(i); // 3

let idade_votando = 17;
if (idade >= 16 && idade_votando < 18) {
    console.log("voto facultativo");
}

let expressao : number = 2;
switch (expressao) {
    case 1: // executado se a expressao = 1;
        console.log("Valor 1");
        break;
    case 2: // executado se a expressao = 2;
        console.log("Valor 2");
        break;
    default: // executado caso a expressão não seja nenhum dos valores;
        console.log("Outro valor");
        break;
};

let numero : number = 100;
numero++;
numero--;
numero += 2;
numero -= 1;
numero *= 4;
numero /= 2;
console.log(numero); // 202

let contador = 1;
console.log(`\niteração 1: `);
while (contador <= 3) {
    console.log(contador);
    contador++;
}

let numeros3 = [4, 5, 6];
console.log(`\niteração 2: `);
for (let i = 0; i < numeros3.length; i++) {
    numeros3[i] = numeros3[i]* 2;
    console.log(numeros3[i]);
}


let numeros4 = [4, 5, 6];

//faz a iteração pelos elementos
console.log(`\niteração 3: `);
for (let numero of numeros4) {
    console.log(numero); // 4, 5, 6
}

//faz a iteração pelos índices
console.log(`\niteração 4: `);
for (let numero_index in numeros4) {
    console.log(`\nindice: ${numero_index}`); // 0, 1, 2
    console.log(`número: ${numeros4[numero_index]}`); // 4, 5, 6
}

function add1(x: number, y: number): number {
    return x + y;
}
console.log(add1(2,3));

var variavel_add = function add2(x: number, y: number): number {
    return x + y;
}
console.log(variavel_add(2,4))

function nomeCompleto(nome: string,
                      sobrenome : string = "Silva"):
                      string {
    return nome + " " + sobrenome;
}
console.log(nomeCompleto('Felipe', 'Gabriel')); // Felipe Gabriel
console.log(nomeCompleto('Felipe')); // Felipe Silva

function somar(...numeros : number[]) {
    let soma = 0;
    for (let numero of numeros){
        soma += numero;
    }
    return soma;
}

console.log(somar()); // 0
console.log(somar(1,2)); // 3
console.log(somar(1,2,3)); // 6 

function dobra1(x : number) : number {
    return 2*x;
}
console.log(dobra1(5)); //10

var dobra2 = (x : number) => 2*x;
console.log(dobra2(2)); //4

let numeros5 : number[] = [1,2,3,4];
numeros5 = numeros5.map(x => 2*x);
console.log(numeros5); //[2,4,6,8]
