
:- use_module(library(clpfd)).
:- use_module(library(clpb)).
:- use_module(library(lists)).

empty(e).

room(ic01).
room(ic04).
room(ic06).
room(ic16).

studentGroup(y1).
studentGroup(y2).
studentGroup(y3).
studentGroup(y4).

roomSlot(ic01,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).
roomSlot(ic04,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).
roomSlot(ic06,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).
roomSlot(ic16,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).

studentGroupSlot(y1,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).
studentGroupSlot(y2,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).
studentGroupSlot(y3,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).
studentGroupSlot(y4,[e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]).

