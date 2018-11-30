package javaLinhaUm;

public class ArvoreBinaria {

	private Node raiz;
	
	
	public Node getRaiz() {
		return raiz;
	}

	public void setRaiz(Node raiz) {
		this.raiz = raiz;
	}

	public Node search(int i) {
		Node pivo = this.raiz;
		while(pivo != null && pivo.getDado() != i) {
			if (pivo.getDado()< i) {
				pivo = pivo.getFilhoDireito();
			}else {
				pivo = pivo.getFilhoEsquerdo();
			}
			
		}
		return pivo;
	}
	
	public Node minimum(Node pivo) {
		
		while (pivo.getFilhoEsquerdo() != null) {
			pivo = pivo.getFilhoEsquerdo();
		}
		return pivo;
	}
	
	public Node maximum(Node pivo) {
		
		while (pivo.getFilhoDireito() != null) {
			pivo = pivo.getFilhoDireito();
		}
		return pivo;
	}
	
	public Node sucessor(Node x) {
		if(x.getFilhoDireito() != null) {
			return minimum(x.getFilhoDireito());
		}
		Node y = x.getPai();
		while(y != null && x.equals(y.getFilhoDireito())) {
			x = y;
			y = y.getPai();
		}
		return y;
	}
	public Node predecessor(Node x) {
		if(x.getFilhoEsquerdo() != null) {
			return maximum(x.getFilhoEsquerdo());
		}
		Node y = x.getPai();
		while(y != null && x.equals(y.getFilhoEsquerdo())) {
			x = y;
			y = y.getPai();
		}
		return y;
	}
	
	public String insert(int num) {
		Node noh = new Node(num);
		Node y = null;
		Node x = this.raiz;
		if(x == null) {
			this.raiz = noh;
			
			return "inserido com sucesso";}
		while(x != null) {
			y = x;
			if(noh.getDado() < x.getDado()) {
				x = x.getFilhoEsquerdo();
			}else {
				x = x.getFilhoDireito();}
		}
		noh.setPai(y);
		if( y == null) {
			this.raiz = noh;
			}
		else if(noh.getDado() < y.getDado()) {
			y.setFilhoEsquerdo(noh);
		}else {
			y.setFilhoDireito(noh);
		}
		return "inserido com sucesso!";
	}

	public static void main(String[] args) {
		ArvoreBinaria a = new ArvoreBinaria();

		a.insert(1);
		a.insert(2);
		a.insert(3);
		System.out.println(a.search(3));
	}

	
	private class Node{
	   private int dado;
	   private Node filhoEsquerdo;
	   private Node filhoDireito;
	   private Node pai;
	   
	   
	public Node(int valor) {
		super();
		this.dado = valor;
	}
	
	public Node() {
		// TODO Auto-generated constructor stub
	}

	public int getDado() {
		return dado;
	}
	public void setDado(int valor) {
		this.dado = valor;
	}
	public Node getFilhoEsquerdo() {
		return filhoEsquerdo;
	}
	public void setFilhoEsquerdo(Node predecessor) {
		this.filhoEsquerdo = predecessor;
	}
	public Node getFilhoDireito() {
		return filhoDireito;
	}
	public void setFilhoDireito(Node sucesso) {
		this.filhoDireito = sucesso;
	}
	public Node getPai() {
		return pai;
	}
	public void setPai(Node pai) {
		this.pai = pai;
	}
	   
	   
		
		
	}
}
