# Resumo de tarefas atrasadas



O relatório Resumo de tarefas atrasadas ajuda a identificar as tarefas que excederam as datas de término previstas.


Para visualizar este relatório, você pode acessar:



> 
> Página inicial > Projetos > Relatórios > Resumo de tarefas atrasadas
> 
> 
> 


O relatório é gerado com base no tipo de documento da tarefa.


![Resumo de tarefas atrasadas](/files/delayed-tasks-summary.png)


### Cálculo do atraso


As tarefas têm um campo de data chamado **Concluído em**, que fica visível quando o status da tarefa é alterado para Concluído.


##### Cenário 1


Se uma tarefa estiver marcada como Concluída e o campo Concluída em estiver definido, o atraso será calculado como a diferença entre Concluída em e a Data de término prevista.



```
Atraso = Concluído em-Data de término prevista

```

##### Cenário 2


Se o campo Concluído em não estiver definido, o atraso será calculado como a diferença entre a data atual e a Data de término prevista.



```
Atraso = Data atual-Data de término prevista

```

### Gráfico


O gráfico mostra o número de tarefas que estão no caminho certo ou atrasadas com base no relatório gerado após a aplicação dos filtros.



