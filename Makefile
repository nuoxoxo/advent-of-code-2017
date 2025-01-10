pre :=	24#22#7#19#10#17#9#8
rmv	:=	rm -f
src	:=  $(if $(shell [ $(pre) -gt 9 ] && echo 1),$(pre).cc,0$(pre).cc)
name	:=	out
comp	:=	c++ -std=c++2a

all	:	$(name)

$(name)	:	$(src)
		@ $(comp) $^ -o $@
		@ ./$(name) < $(pre).0

test	:	$(name)
		@#@ ./$(name) < $(pre).0
		@ echo "\n------\ntest\n------\n"
		@ ./$(name) < $(pre).1
		@ make f

clean	:
		@ $(rmv) $(name)
fclean	:	clean
		@ $(rmv) out *.out
t		: test
f	:	fclean
re	:	f all
.PHONY	:	fclean clean f all re
