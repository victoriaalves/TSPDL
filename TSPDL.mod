/* Instância pequena do TSPDL para testar formulação
 *
 * Modelagem em MathProg do Traveling Salesman Problem with Draft Limits
 * 
 * Para resolver, execute a seguinte linha de comando.
 * Lembrando que a solução será gravada no arquivo TSPDL.sol.
 *
 * $ glpsol -m TSPDL.mod -d TSPDL.dat -o TSPDL.sol
 *
 * Arquivo: TSPDL.mod, modela o problema com dados de entrada completamente 
 * separados do modelo de programação linear. Confira o arquivo de dados
 * TSPDL.dat.
 *
 * Autores: Christian Schmitz e Victoria Alves
 * 2019/1
 */

# Conjuntos
# conjunto de portos 
set V;

# garagem em V = 1
set Vg := { 1 };

# conjunto dos portos consumidores
set Vc := V diff Vg;

# Parâmetros
param d{j in V};
/* parâmetro de cada porto com uma demanda >= 0 */

param l{j in V};
/* parâmetro de cada porto com limite de profundidade >= 0 */

param custo{i in V, j in V};
/* parâmetro de custo da viagem de um porto V para outro porto V */

# Variáveis
var x{i in V, j in V} >= 0 binary;
/* definir se a visita do porto i é antes do porto j */

var y{i in V, j in V} >= 0;
/* indicam a quantidade de carga da embarc durante a viagem entre os portos (i,j) */

# Função Objetivo
minimize total: sum{i in V, j in V} custo[i,j] * x[i,j];
/* função objetivo */

# Restrições
s.t. c1 {j in V}: sum{i in V} x[i,j] = 1;
/* restrição 19 */

s.t. c2 {i in V}: sum{j in V} x[i,j] = 1;
/* restrição 20 */

s.t. c3 {j in Vc}: sum{i in V} y[i,j] - sum{i in V} y[j,i] = d[j];
/* restrição 21 */

s.t. c4: sum{j in V} y[1,j] = sum{i in Vc} d[i];
/* restrição 22 */

s.t. c5: sum{i in V} y[i,1] = 0;
/* restrição 23 */ 

s.t. c6 {i in V, j in V}: y[i,j] <= l[j] * x[i,j]; 
/* restrição 24 */

end;
