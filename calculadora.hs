--Calculadora con funciones 
--Sergio Luis Huanca Cuellar
--INF -319 2do Parcial
--Pregunta 1

--entrada de datos
getnum::IO Integer
getnum = do
  s <- getLine
  return (read s)
--funcion suma
suma :: Integer -> Integer -> Integer
suma x y = x + y
--funcion resta
res :: Integer -> Integer -> Integer
res x y = x - y
--funcion multiplicacion
mul :: Integer -> Integer -> Integer
mul x y = x * y
--funcion division
divi :: Integer -> Integer -> Integer
divi x y = if y == 0 then -1 else x `div` y

  
calcu = do
-- calculadora funciones
  putStrLn("****CALCULADORA EN HASKELL CON FUNCIONES****")
--introduce dos numeros  
  putStr("Numero 1:\n")
  n1 <- getnum
  putStr("Numero 2:\n")
  n2 <- getnum
--suma
  putStr "La suma es: "
  print (suma n1 n2)
 --resta
  putStr "La resta es: "
  print (res n1 n2)
 --multiplicacion
  putStr "La multiplicacion es: "
  print (mul n1 n2)
 --division
  putStr "La divsion es: "
  print (divi n1 n2)
 



