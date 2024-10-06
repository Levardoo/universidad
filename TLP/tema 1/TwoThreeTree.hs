{-# LANGUAGE DeriveFoldable #-}
{-# LANGUAGE DeriveFunctor  #-}

module TwoThreeTree where
import Repaso (recTree)


data TwoThreeTree a = Empty
                    | Leaf a
                    | Two a (TwoThreeTree a) (TwoThreeTree a)
                    | Three a a (TwoThreeTree a)  (TwoThreeTree a) (TwoThreeTree a)
                   deriving (Show, Functor, Foldable)

plegar :: b -> (a->b) -> (a -> b -> b -> b) -> (a->a->b->b->b->b) -> TwoThreeTree a -> b
plegar e l two three t = recTree23 t
    where
        recTree23 Empty = e
        recTree23 (Leaf x) = l x
        recTree23 (Two x i d) = two x (recTree23 i) (recTree23 d)
        recTree23 (Three x y i c d) =three x y (recTree23 i) (recTree23 c) (recTree23 d)

sumar t = plegar 0 id (\x si sd -> x+ si+sd) (\x y si sc sd -> x + y+ si+sc+sd) t

tree :: TwoThreeTree Int
tree = Three 1 10
             (Two 2
                  (Leaf 3)
                  (Two 4
                       Empty
                       (Leaf 4)))   
             (Three 5 50
                 (Leaf 6)
                 (Leaf 7)
                 (Leaf 8))
             (Two 9
                 (Leaf 10)
                 Empty
             )
