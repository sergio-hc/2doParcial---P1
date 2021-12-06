//Calculadora con funciones en Scala
//Sergio Luis Huanca Cuellar
//Segundo Parcial - problema 1

object calculadora {
  //funcion sumar
  def sumar(x: Int, y: Int): Int =  x + y
  //funcion restar
  def restar(x: Int, y: Int): Int = x - y
  
  def multiplicar(x: Int, y: Int): Int =   x * y

  def dividir(x: Int, y: Int): Int = 
    y match {
      case 0 => -1
      case _ => x/y
  }
//funcion calculadora
 def calcu(x:Int, y:Int, operacion:String):Int={
  operacion match {
  case "suma"=>sumar(x,y)
  case "resta"=>restar(x,y)
  case "multi"=>multiplicar(x,y)
  case "divi"=>dividir(x,y)
  case _ => -1
  }
} 

def main(args: Array[String]):Unit = {
  println("*****CALCULADORA EN SCALA CON FUNCIONES******")
  //valores
  val a = 100
  val b = 20
  println("Los valores a operar son: "+ a +","+ b)
//suma
  println("Suma: "+calcu(a,b,"suma")) // numero a operar  4 5 
//resta
  println("Resta: "+ calcu(a,b,"resta"))
  //multi
  println("Multiplicacion: "+ calcu(a,b,"multi"))
  //divi
  println("Division: "+ calcu(a,b,"divi"))
}
}