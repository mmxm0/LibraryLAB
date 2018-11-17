package labLib;

public class ListaDuplamenteEncadeada{
	
	private Node inicio;
	private Node fim;
	private int len;
	
	
	
	
	public Node getInicio() {
		return inicio;
	}




	public Node getFim() {
		return fim;
	}


	public int getLen() {
		int saida =0;
		if(!isEmpty()) {
			Node k = this.inicio;
			while(k !=null) {
				saida++;
				k = k.getProximo();
			}
		}
		
		return saida;
	}

	public void setInicio(Node inicio) {
		this.inicio = inicio;
	}
	public void setFim(Node fim) {
		this.fim = fim;
	}

	public Boolean isEmpty() {
		Boolean s;
		if(this.inicio == null) {
			s = true;
		}else {s = false;}
		return s;
	}

	private void insere(String i) {
		Node no = new Node(i);
		if(isEmpty()) {
			this.inicio = no;
			this.fim = no;
		}
		else {
			this.fim.setProximo(no);
			no.setAnterior(this.fim);
			this.fim = no;
		
		}
		this.len = getLen();
		
	}
	
	private Node pesquisar(String dado) {
		Node i = new Node();
		if(isEmpty()) {
			System.out.println("Erro, Lista Vazia");

		}else {
			Node novo = new Node(dado);
			i = this.inicio;
			while (!novo.getDado().equals(i.getDado())) {
				i = i.getProximo();
				if (i == null) { break;}
				
			}
		}
		return i;
	}
	
	
	private String excluir(String dado) {
		String saida;
		if(isEmpty()) {
			saida = "Erro ao excluir, lista vazia!";
		}
		else if(this.inicio.equals(this.fim)){
			this.inicio = null;
			this.fim = null;
			saida = this.inicio.getDado();
		}else {
			Node pivo = pesquisar(dado);
			
			if(pivo == null) {
				saida = "Erro, elemento não está na lista";
			
			//Remover primeiro elemento
			}else if(pivo.getAnterior() == null) {
				saida = pivo.getDado();
				Node prox = pivo.getProximo();
				prox.setAnterior(null);
				pivo.setAnterior(null);
				this.inicio = prox;
			
			//Remover ultimo elemento	
			}else if(pivo.getProximo() == null) {
				saida = pivo.getDado();
				Node ant = pivo.getAnterior();
				ant.setProximo(null);
				pivo.setProximo(null);
				this.fim = ant;
			}else {
				saida = pivo.getDado();
				Node prox = pivo.getProximo();
				Node ant = pivo.getAnterior();
				prox.setAnterior(ant);
				ant.setProximo(prox);
				pivo.setAnterior(null);
				pivo.setProximo(null);
				
			}
		}
		
		return saida;
	}
	
	private String listar() {
		String saida="";
		if(!isEmpty()) {
			Node k = this.inicio;
			while(k != null) {
				saida+=k.getDado()+" ";
				k = k.getProximo();
			}
		}else {saida = "null";}
		return saida;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListaDuplamenteEncadeada l = new ListaDuplamenteEncadeada();
		l.insere("100");
		l.insere("10");
		l.insere("20");

		System.out.println(l.listar());
		String e = l.excluir("10");
		int t = l.getLen();
		System.out.println(l.listar());
	}

	

	public static class Node{

		private Node anterior;
		private Node proximo;
		private String dado;
		
		
		public Node() {
			super();
			// TODO Auto-generated constructor stub
		}
		public Node(String dado) {
			super();
			this.dado = dado;
		}
		public Node getAnterior() {
			return anterior;
		}
		public void setAnterior(Node anterior) {
			this.anterior = anterior;
		}
		public Node getProximo() {
			return proximo;
		}
		public void setProximo(Node proximo) {
			this.proximo = proximo;
		}
		public String getDado() {
			return dado;
		}
		public void setDado(String dado) {
			this.dado = dado;
		}
		
		
	}

	

}

