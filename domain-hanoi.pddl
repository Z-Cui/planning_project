; pddlfile

(define (domain hanoi)
  (:requirements :strips)
  (:predicates (clear ?x)
	       (on ?x ?y)
	       (smaller ?x ?y)
	       (disk ?d)
	       )
  
  (:action move
      :parameters (?d ?from ?to)
      :precondition (
        and (on ?d ?from)
          (smaller ?d ?to)
          (clear ?d)
          (clear ?to)
      )
      :effect (
        and (not (on ?d ?from))
          (on ?d ?to)
          (clear ?from)
          (not (clear ?to))
      )
  )
)
  
