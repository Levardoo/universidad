{-

Programming Languages
Fall 2024

Semantics of Arithmetic Expressions

-}

module Aexp where
import Language.Haskell.TH (Lit)
import GHC.Base (TYPE)
import Data.Set

-- |----------------------------------------------------------------------
-- | Exercise 1 - Abstract Syntax and Semantics of Aexp
-- |----------------------------------------------------------------------
-- | Define the algebraic data type 'Aexp' for representing arithmetic
-- | expressions.

type VarId = String
type LitNum = String
-- DEFINO EL TIPO DE DATOS Aexp QUE REPRESENTA EXPRESIONES ARITMETICAS
data  Aexp  = NumLit LitNum 
            | Var VarId 
            | Add Aexp Aexp
            | Mul Aexp Aexp
            | Sub Aexp Aexp
            deriving Show

-- (X * 3) + (y - 5)
exp0 :: Aexp
exp0 = Add (Mul (Var "x") (NumLit "3")) (Sub (Var "y") (NumLit "5"  ))


type Z = Integer
type State = VarId -> Z

-- supongamos que s0 = {x -> 5, y -> 7, z -> -2}
s0 :: State
s0 "x" = 5
s0 "y" = 7
s0 "z" = -2
s0 _ = 0

-- | Define the function 'aval' that computes the value of an arithmetic
-- | expression in a given state.

--Me guio por la sintaxis de Aexp para definir la funcion aVal
nVal :: LitNum -> Z
nVal n = read n

aVal :: Aexp -> State ->Z
aVal (NumLit n) s = nVal n
aVal (Var n) s = s n
aVal (Add a1 a2) s = aVal a1 s + aVal a2 s
aVal (Mul a1 a2) s = aVal a1 s * aVal a2 s
aVal (Sub a1 a2) s = aVal a1 s - aVal a2 s



-- |----------------------------------------------------------------------
-- | Exercise 2 - Free variables of expressions
-- |----------------------------------------------------------------------
-- | Define the function 'fvAexp' that computes the set of free variables
-- | occurring in an arithmetic expression. Ensure that each free variable
-- | occurs only once in the resulting list.

fvAexp :: Aexp -> [VarId] 
fvAexp (NumLit _) = []
fvAexp (Var x) = [x]
fvAexp (Add a1 a2) = fvAexp a1 ++ fvAexp a2
fvAexp (Mul a1 a2) = fvAexp a1 ++ fvAexp a2
fvAexp (Sub a1 a2) = fvAexp a1 ++ fvAexp a2 

-- |----------------------------------------------------------------------
-- | Exercise 3 - Substitution of variables in expressions
-- |----------------------------------------------------------------------
-- | Define the algebraic data type 'Subst' for representing substitutions.

data Subst = VarId :->: Aexp

-- | Define a function 'substAexp' that takes an arithmetic expression
-- | 'a' and a substitution 'y -> a0' and returns the substitution 'a [y -> a0]';
-- | i.e., replaces every occurrence of 'y' in 'a' by 'a0'.

substAexp :: Aexp -> Subst -> Aexp
substAexp (NumLit n) _ = NumLit n
substAexp (Var x) (y :->: a0) = if x == y then a0 else Var x 

-- |----------------------------------------------------------------------
-- | Exercise 4 - Update of state
-- |----------------------------------------------------------------------
-- | Define the algebraic data type 'Update' for representing state updates.

data Update = VarId :=>: Z

-- | Define a function 'update' that takes a state 's' and an update 'x -> v'
-- | and returns the updated state 's [x -> v]'

update :: State -> Update -> State
update s (y :=>: v) = \x -> if x == y then v else s x 
--update s (y :=>: v) x = if x == y then v else s x



-- | Define a function 'updates' that takes a state 's' and a list of updates
-- | 'us' and returns the updated states resulting from applying the updates
-- | in 'us' from head to tail. For example:
-- |
-- |    updates s {x -> 1, y > 2, x -> 3}
-- |
-- | returns a state that binds 'x' to 3 (the most recent update for 'x').

updates :: untyped
updates = undefined

-- |----------------------------------------------------------------------
-- | Exercise 5 - Folding expressions
-- |----------------------------------------------------------------------
-- | Define a function 'foldAexp' to fold an arithmetic expression.
-- Los plegados se pueden deducir a partir de la definición del tipo algebraico     


foldAexp :: (LitNum -> b) -> (VarId -> b) -> (b -> b -> b) -> Aexp -> b
foldAexp nl v add a = recAexp a
    where
        recAexp (NumLit n) = nl n
        recAexp (Var x) = v x
        recAexp (Add a1 a2) = add (recAexp a1) (recAexp a2)

-- | Use 'foldAexp' to define the functions 'aVal', 'fvAexp', and 'substAexp'.

aVal' :: untyped
aVal' = undefined

fvAexp' :: untyped
fvAexp' = undefined

substAexp' :: untyped
substAexp' = undefined
