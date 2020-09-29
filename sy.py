#medianas = [19,16,16,15,17,14,13,14,11,13,15,14,12,12,1];
#medianas  = [16,12,12,10,15,10,10,12,7,11,12,11,10,10,1];
medianas = [17,15,15,11,16,11,12,13,8,11,12,11,11,11,1];

locais = ['Casa Sherlock','Museu','Bar','Farmacia','Scotland Yard','Banco','Teatro','Penhores','Parque','Docas','Livraria','Chaveiro','Charutaria','Hotel','Carruagens'];


def idxParaLocais(caminho) :
	locaisAtual = [];
	i = 0;
	while (i < 15) :
		locaisAtual.append(locais[caminho[i]]);
		i += 1;
	return locaisAtual;

def visita (idx,atual,visitado,caminhoAtual,distAtual,menorCaminho,distMenorCaminho) :
	if (idx == 15) :
		distAtual += dist[atual][0];
		#print distAtual		
		if (distAtual <= distMenorCaminho[0]) :
			distMenorCaminho[0] = distAtual;
			print distAtual;			
			print idxParaLocais(caminhoAtual);
		return
	else :
		#ainda nao visitei todo mundo
		#print caminhoAtual;
		i = 1;

		while i < 15 :			
			if visitado[i] == 0 and dist[atual][i] <= medianas[atual]:
				visitado[i] = 1;
				caminhoAtual.append(i);
				distAtual += dist[atual][i];
				visita(idx+1,i,visitado,caminhoAtual,distAtual,menorCaminho,distMenorCaminho);				
				distAtual -= dist[atual][i];
				caminhoAtual.pop();
				visitado[i] = 0;
			i = i + 1;


dist = [[0,7,10,17,17,25,29,13,20,16,19,23,25,24,33],[7,0,15,16,22,24,28,12,15,11,12,16,20,17,28],[10,15	,0	,9	,15	,17	,21	,7	,12	,16	,19	,23	,17	,24	,25],[17	,16	,9	,0	,8	,10	,14	,8	,11	,15	,20	,24	,16	,24	,18],[17	,22	,15	,8	,0	,12	,16	,14	,17	,21	,26	,27	,18	,26	,20],[25	,24	,17	,10	,12	,0	,6	,14	,11	,21	,21	,17	,8	,16	,10],[29	,28	,21	,14	,16	,6	,0	,16	,7	,13	,17	,13	,4	,12	,10],[13	,12	,7	,8	,14	,14	,16	,0	,9	,13	,14	,18	,14	,16	,22],[20	,15	,12	,11	,17	,11	,7	,9	,0	,6	,12	,8	,5	,7	,15],[16	,11	,16	,15	,21	,21	,13	,13	,6	,0	,7	,11	,11	,12	,23],[19	,12	,19	,20	,26	,21	,17	,14	,12	,7	,0	,6	,15	,7	,18],[23	,16	,23	,24	,27	,17	,13	,18	,8	,11	,6	,0	,11	,3	,14],[25	,20	,17	,16	,18	,8	,4	,14	,5	,11	,15	,11	,0	,10	,12],[24,17,24,24,26,16,12,16,7,12,7,3,10,0,11],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]];


distMenorCaminho = [100000000000];
menorCaminho = [];

distAtual = 0;
caminhoAtual = [0];

visitado = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

visita(1,0,visitado,caminhoAtual,distAtual,menorCaminho,distMenorCaminho);

