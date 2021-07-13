<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
</head>
<body>

<h1><center>Relatório do Projecto Final [Recurso] </center></h1>

<h2><center> Fundamentos de Programação </center></h2>  

<center><p><img src="https://i.pinimg.com/564x/bc/26/4c/bc264ca6d03e336926220dbfef353ac6.jpg" width="600"  /></p></center>


<h4><center> Projecto de Recurso: Sheep & Wolf </center></h4>  

<center>Versão # 1.0</center>

<center>Terça, Julho 13, 2021</center>

<div style="page-break-after:always"></div>


<h2>Tabela de Conteúdos</h2>

<ol>
<li><a href="#informaçãobase">Informação Base</a></li>
<li><a href="#sumario">Sumário do Projecto</a>
<ol>
<li><a href="#regras">Regras do Jogo</a>
<li><a href="#controlos">Controlos dos Jogadores</a>
</ol></li>
<li><a href="#menu">Menu Inicial</a>
<li><a href="#tabuleiro">Tabuleiro</a>
<li><a href="#movimentos">Movimentos do Jogador</a></li>
<li><a href="#contribuiçoes">Contribuições individuais</a></li>
</ol></li>


<div style="page-break-after: always"></div>


<h3>1. Informação Base <a name="informaçãobase"></a></h3>

<p> 

**Nome do Projecto**

Projecto de Recurso: Sheep & Wolf


**Membros do Projecto**

Rafaela Henriques 22005252
`Github Username: rafaelahenriques`

Sónia Raposo 22000344
`Github Username Sonia-Raposo `

Steven Hall 22001753
`Github Username: bryanb619`


**Data de Completação do Projecto**

13.07.2021

</p>
 

<p>


<h3>2. Sumário do Projecto <a name="sumario"></a></h3>

Este projecto consiste na construção de um tabuleiro de jogo 2D divido em 8x8 casas onde dois jogadores jogam um contra o outro.

De um lado do tabuleiro, um jogador controla os **Lobos** e no lado oposto do tabuleiro, outro jogador controla as **Ovelhas**.


</p>

<p>

<h4>2.1 Regras do Jogo <a name="regras"></a></h4>

Os jogadores jogam à vez e apenas conseguem movimentar-se uma casa na diagonal por cada turno. Para movimentarem-se, é utilizado o rato.

**Para o jogador que controla os Lobos ganhar:** 
* Garantir que a ovelha não tem mais movimentos possiveis.

**Para o jogador que controla as Ovelhas ganhar:**
* Garantir que a ovelha chega ao topo do tabuleiro.

<h4>2.2 Controlos dos Jogadores<a name="controlos"></a></h4>

**Movimentos do Jogador que controla os Lobos:**
* Apenas podem movimentar-se nas diagonais para baixo

**Movimentos do Jogador que controla as Ovelhas:**
* Podem movimentar-se nas diagonais para cima ou para baixo



</p>


<p>

<h3>3. Menu Inicial <a name="menu"></a></h3>

Para a criação do Menu Incial foi criado um ficheiro ***py: Menu***.

**O Menu tem as opções:**
* Start (Inicia o jogo de tabuleiro)
* Quit (Sai da aplicação do jogo)

**É neste ficheiro de menu onde é:**
* Determinado a *Altura e Largura* do Menu
* Determinado o *limite de FPS* (Frames per Second)
* Inseridas as *fonts* utilizadas no texto do Menu
* Inserido os *ficheiros de audio* para a música e sons de navegação de Menu
* Inseridas as *imagens* de Fundo, da Ovelha e do Lobo que aparecem no Menu
* Definidas as teclas do Teclado para navegação do Menu



 </p>

 <p>

<h3>4. Tabuleiro (FALTA) <a name="tabuleiro"></a></h3>


Para a criação do tabuleiro foi criado um ficheiro ***py: Main***. 

(FALTA)


O tipo de mapa criado é um **text_map** em 2D para a contrução do mesmo foi utilizada a letra **I**.

Para criar o mapa em si, são detectadas as letras **I** através de uma *função if* que transforma a letra numa parede.

Sendo assim, foram criados os limites do mapa, colocando **I** nos cantos superior, inferior e lateral no **text_map**, e colocadas paredes dentro do mapa, intercalando com "." que representa espaço vazio.

Para transformar este mapa 2D numa vista 3D, é utilizada a fórmula que se encontra no ficheiro ***py: AppSettings***:

Multiplicamos ainda distancia por 3, para optimizar a escala
Isso faz com que o escala do cenário seja "aumentada"

`proj_3d = 3 * dist * walls`

Sendo que a multiplicação por da distância por 3 serve para projectar e optimizar a escala tornando assim a vista e a navegação pelo mapa de forma mais agradável para o jogador devido à escala mais realista. 

</p>

<p>

<h3>5. Movimentos do Jogador (FALTA) <a name="movimentos"></a></h3>

Para definir as configurações do jogo, foi criado um ficheiro ***py: AppSettings***.

É neste ficheiro que são definidas as configurações tais como:

**Configurações de ecrã**
* Largura e Altura da tela de jogo
* FPS (Valor Limite de Frames por Second)

**Configurações Ray Casting**
* Ponto de Vista
* Número de raios
* Dimensão
* Distância
* Projecção 3D
* Ângulo
* Escala

**Configurações de cores do jogo**
* Lista de cores em código RGB usadas no jogo

</p>


<h3>6.Contribuições individuais (FALTA)<a name="contribuiçoes"></a></h3>

**Rafaela Henriques**
* Organização e correções de código
* Criação do ficheiro ***Menu***
* Criação do ficheiro ***Main***

**Sónia Raposo**
* Organização e correções de código
* Realização da Arte (Lobo, Ovelha e Fundo)
* Realização do ficheiro ***readme***
* Realização do ficheiro ***Postmortem***

**Steven Hall**
* Organização e correções de código
* Configurações Base
* Criação do ficheiro ***Ray***
* Configurações dos Visuais do Jogo em 3D
* Movimentos especiais do jogador (Sprint e Salto)
* Configurações de Cores no Mapa