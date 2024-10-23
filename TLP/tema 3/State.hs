-- State.hs - Implementation of State

module State where

type  Var    =  String
type  Z      =  Integer
type  State  =  Var -> Z

sInit :: State
sInit "x" =  3
sInit _   =  0


update :: State -> Var -> Z -> State 
update s x z = \ v -> if v == x then z else s v

