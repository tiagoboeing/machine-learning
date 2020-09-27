# Aprendizado de máquina

Esta aplicação utiliza Python para o processamento dos treinamentos, Electron + ReactJS para a aplicação desktop e frontend.

A comunicação entre Python e Electron ocorre via eventos, como se fosse uma bridge (`IpcMain` e `IpcRenderer`)

## Informações

### Personagens escolhidos

- Apu Nahasapeemapetilon
- Merge Simpson

### Características analisadas

#### Apu Nahasapeemapetilon

- Cor da pele
- Cor da jaqueta/camiseta
- Cor da calça

#### Merge Simpson

- Cor da pele
- Cor do cabelo
- Cor do vestido

### Extraindo características

#### Range de cores

Analisando cores e aplicando faixa de tolerância (range) para cada um dos personagens e característica desejada:

|![](https://i.imgur.com/QHVoClY.png)|![](https://i.imgur.com/mYEPBS0.png)|![](https://i.imgur.com/CvMuTWF.png)|

Apu Nahasapeemapetilon

<table width="100%">
  <tr>
    <th colspan="4">Cor da pele</th>
    <th></th>
    <th colspan="3">Cor da calça</th>
    <th></th>
    <th colspan="3">Cor da camisa</th>
  </tr>
  <tr>
    <td>R</td>
    <td>145</td>
    <td>100</td>
    <td>200</td>
    <td></td>
    <td>202</td>
    <td>189</td>
    <td>200</td>
    <td></td>
    <td>36</td>
    <td>28</td>
    <td>60</td>
  </tr>
  <tr>
    <td>G</td>
    <td>66</td>
    <td>30</td>
    <td>130</td>
    <td></td>
    <td>189</td>
    <td>175</td>
    <td>210</td>
    <td></td>
    <td>104</td>
    <td>95</td>
    <td>150</td>
  </tr>
  <tr>
    <td>B</td>
    <td>35</td>
    <td>0</td>
    <td>50</td>
    <td></td>
    <td>137</td>
    <td>119</td>
    <td>200</td>
    <td></td>
    <td>17</td>
    <td>0</td>
    <td>35</td>
  </tr>
  <tr>
    <td></td>
    <td>Alvo</td>
    <td colspan="2" align="center">Range</td>
    <td></td>
    <td>Alvo</td>
    <td colspan="2" align="center">Range</td>
    <td></td>
    <td>Alvo</td>
    <td colspan="2" align="center">Range</td>
  </tr>
</table>

-------

Merge Simpson

<table width="100%">
  <tr>
    <th colspan="4">Cor da pele</th>
    <th></th>
    <th colspan="3">Cor do cabelo</th>
    <th></th>
    <th colspan="3">Cor do vestido</th>
  </tr>
  <tr>
    <td>R</td>
    <td>205</td>
    <td>202</td>
    <td>235</td>
    <td></td>
    <td>65</td>
    <td>80</td>
    <td>40</td>
    <td></td>
    <td>142</td>
    <td>105</td>
    <td>166</td>
  </tr>
  <tr>
    <td>G</td>
    <td>171</td>
    <td>158</td>
    <td>195</td>
    <td></td>
    <td>85</td>
    <td>79</td>
    <td>110</td>
    <td></td>
    <td>171</td>
    <td>135</td>
    <td>215</td>
  </tr>
  <tr>
    <td>B</td>
    <td>11</td>
    <td>0</td>
    <td>50</td>
    <td></td>
    <td>253</td>
    <td>145</td>
    <td>255</td>
    <td></td>
    <td>91</td>
    <td>0</td>
    <td>123</td>
  </tr>
  <tr>
    <td></td>
    <td>Alvo</td>
    <td colspan="2" align="center">Range</td>
    <td></td>
    <td>Alvo</td>
    <td colspan="2" align="center">Range</td>
    <td></td>
    <td>Alvo</td>
    <td colspan="2" align="center">Range</td>
  </tr>
</table>


## Utilização

Já existe um arquivo de classificação onde o treinamento foi realizado com todas as imagens de ambos os personagens. Basta testar com uma imagem externa e classificar.

> Ao rodar o programa será possível realizar o treinamento com todo o dataset (**este processo pode levar horas**).

