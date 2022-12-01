# minera_ana
<h2>Pega informações do google a partir de determinadas informções disponibilizadas, sendo estas:</h2>
  
  <h4>assunto: Determina o tópico a ser pesquisado, podendo ser uma palavra ou expressão</h4>
  
    Exemplo: violencia ou Violência Doméstica ( Note que é possível escrever com letras maiúsculas ou acentos ).
      
  <h4>estado: Determina o estado a ser pesquisado</h4>
  
    Exemplo: Paraná ou mato grosso do sul ( Note que é possível escrever com letras maiúsculas ou acentos ).
       
  <h4>site: Específica o site ao qual deseja ser pesquisado</h4>
  
    Exemplo: g1.com ou folha.uol
       
  <h4>periodo_de e periodo-fim: Especificam o início e fim da faixa temporal a qual deseja-se pesquisar</h4>
  
    Exemplo: 01/1/2000 ou 10/8/2015 (Note que é possível escrever tanto valores unitários com zeros (0) quanto sem zeros (0))
       
  <h4>A estrutura abaixo pode ser encontrada no código:</h4>
    
    assunto = 'violencia' 
    estado = 'mato grosso do sul'
    site = 'g1.com'
    periodo_de = '1/1/2021'
    periodo_fim = '1/1/2022'

  <h4>Tendo esta estrutura em mente só é necessário escrever nas lacunas as palavras e expressões chaves para que o código faça a pesquisa.</h4>
