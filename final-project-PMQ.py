def compute_first(symbol, grammar, first_sets):
    if symbol.islower():
        return {symbol}

    if symbol in first_sets:
        return first_sets[symbol]

    first_sets[symbol] = set()
    
    for production in grammar.get(symbol, []):
        for prod_symbol in production:
            if prod_symbol.islower():
                first_sets[symbol].add(prod_symbol)
                break
            elif prod_symbol != 'e':
                first_sets[symbol].update(compute_first(prod_symbol, grammar, first_sets))
            if 'e' not in first_sets.get(prod_symbol, set()):
                break
        else:
            first_sets[symbol].add('e') 
    
    return first_sets[symbol]


def compute_follow(symbol, grammar, first_sets, follow_sets, start_symbol):
    if symbol == start_symbol and not follow_sets[symbol]:
        follow_sets[symbol].add('$')
    
    for nonterminal, productions in grammar.items():
        for production in productions:
            for i, prod_symbol in enumerate(production):
                if prod_symbol == symbol:
                    if i + 1 < len(production):
                        next_symbol = production[i + 1]
                        if next_symbol.islower():
                            follow_sets[symbol].add(next_symbol)
                        else:
                            follow_sets[symbol].update(first_sets[next_symbol] - {'e'})
                    if i + 1 == len(production) or 'e' in first_sets.get(production[i + 1], set()):
                        follow_sets[symbol].update(follow_sets[nonterminal])

    return follow_sets[symbol]


def parse_input():
    n_cases = int(input())
    cases = []
    
    for _ in range(n_cases):
        m = int(input())
        grammar = {}
        
        for _ in range(m):
            rule = input().split()
            nonterminal = rule[0]
            productions = rule[1:]
            grammar[nonterminal] = productions
            if '$' in productions or 'e' in productions:
                exit()

        start_symbol_in_first_derivation = False
        nonterminal, productions = next(iter(grammar.items()))
        if 'S' == nonterminal:
            start_symbol_in_first_derivation = True
                
        if not start_symbol_in_first_derivation:
            exit()
        
        cases.append((grammar, m))

    return cases


def print_sets(first_sets, follow_sets):
    for nonterminal in sorted(first_sets.keys()):
        print(f"First({nonterminal}) = {{{', '.join(sorted(first_sets[nonterminal]))}}}")
    
    for nonterminal in sorted(follow_sets.keys()):
        print(f"Follow({nonterminal}) = {{{', '.join(sorted(follow_sets[nonterminal]))}}}")


def main():
    cases = parse_input()
    
    for grammar, m in cases:
        first_sets = {}
        follow_sets = {nt: set() for nt in grammar}
        
        for nonterminal in grammar:
            compute_first(nonterminal, grammar, first_sets)
        
        for nonterminal in grammar:
            compute_follow(nonterminal, grammar, first_sets, follow_sets, 'S')
        
        print_sets(first_sets, follow_sets)
        print()

if __name__ == "__main__":
    main()
