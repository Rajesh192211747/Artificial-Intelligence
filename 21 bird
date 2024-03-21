can_fly(eagle).
can_fly(sparrow).
can_fly(pigeon).

cannot_fly(penguin).
cannot_fly(ostrich).

can_bird_fly(Bird) :- can_fly(Bird),write('.It Can Fly').
can_bird_fly(Bird) :- write('.It cannot Fly'),\+ cannot_fly(Bird).
