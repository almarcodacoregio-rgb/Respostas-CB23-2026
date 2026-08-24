1\)  
A Classe Funcionário herdaria da Classe Pessoa os seguintes atributos:( nome, idade)  
	Pois, todo funcionário possui nome e idade.

A Classe Garçom herdaria da Classe Pessoa os seguintes atributos:( nome, idade)  
	Pois, todo garçom possui nome e idade.  
A Classe Garçom herdaria da Classe Funcionário os seguintes atributos:( salario, carga\_horaria )  
	Pois, todo garçom possui salário e carga horária.

A Classe Chefe de cozinha herdaria da Classe Pessoa os seguintes atributos:( nome, idade)  
	Pois, todo chefe de cozinha possui nome e idade.  
A Classe Chefe de cozinha herdaria da Classe Funcionário os seguintes atributos:( salario, carga\_horaria )  
	Pois, todo chefe de cozinha possui salário e carga horária.

A Classe Gerente herdaria da Classe Pessoa os seguintes atributos:( nome, idade)  
	Pois, todo gerente possui nome e idade.  
A Classe Gerente herdaria da Classe Funcionário os seguintes atributos:( salario, carga\_horaria )  
	Pois, todo gerente possui salário e carga horária.

A Classe Pizzaria herdaria da Classe Restaurante os seguintes atributos:( nome, endereco, telefone)  
	Pois, toda pizzaria possui nome, endereço e telefone.

A Classe Bolo herdaria da Classe Iguaria (comida) os seguintes atributos:( nome, preco)  
	Pois, todo bolo possui nome e preço.

A Classe Pizza herdaria da Classe Iguaria (comida) os seguintes atributos:( nome, preco)  
	Pois, toda pizza possui nome e preço.

2\)  
Sugiro que a Classe Restaurante possua o atributo menu, que contenha uma lista de instâncias da Classe Iguaria. Uma lista seria o ideal, pois o menu poderia ser mudado depois.

3\)  
Garçom \- ( anotar\_pedido ) seria do tipo: Iguaria  
Chefe de cozinha \- ( preparar ) seria do tipo: Iguaria  
Gerente \- ( demitir ) seria do tipo: Funcionário

O tipo apropriado seria Classe nesses casos, pois carregaria as informações necessárias.

