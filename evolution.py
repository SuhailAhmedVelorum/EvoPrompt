def ape(args, evaluator):
    from evoluter import ParaEvoluter

    evoluter = ParaEvoluter(args, evaluator)
    evoluter.evolute(mode=args.para_mode)

def ga_evo(args, evaluator):
    from evoluter import GAEvoluter

    evoluter = GAEvoluter(args, evaluator)
    evoluter.evolute()


def de_evo(args, evaluator):
    from evoluter import DEEvoluter

    evoluter = DEEvoluter(args, evaluator)
    evoluter.evolute()

def pso_evo(args, evaluator):
    from evoluter import PSOEvoluter

    evoluter = PSOEvoluter(args, evaluator)
    evoluter.evolute()

def gwo_evo(args, evaluator):
    from evoluter import GWOEvoluter

    evoluter = GWOEvoluter(args, evaluator)
    evoluter.evolute()