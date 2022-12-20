#comp	:=	c++ -std=c++11 -Wall -Werror -Wextra
comp	:=	c++ -std=c++17
name	:=	out
rmv	:=	rm -f

src	:=	aoc1701.cc

all	:	$(name)
$(name)	:	$(src)
		@ $(comp) $^ -o $@
		@ echo "data" && echo "" 
		@ ./$(name) < _inputs_/1701.0
		@ echo "" && echo "test" && echo ""
		@ ./$(name) < _inputs_/1701.1
		@ make f

clean	:
		@ $(rmv) $(name)

fclean	:	clean
		@ $(rmv) out *.out

f	:	fclean
re	:	f all
.PHONY	:	fclean clean all re f
