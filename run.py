from args import parse_args
from evolution import ape, gwo_evo, pso_evo
from utils import set_seed
from evaluator import CLSEvaluator, SimEvaluator, SumEvaluator

def run(args):
    set_seed(args.seed)
    task2evaluator = {
        "cls": CLSEvaluator,
        "sum": SumEvaluator,
        "sim": SimEvaluator,
    }
    evaluator = task2evaluator[args.task](args)
    evaluator.logger.info(
        "---------------------Evolving prompt-------------------\n"
    )
    if args.evo_mode == "para" and args.para_mode == "topk":
        ape(args=args, evaluator=evaluator)
    elif args.evo_mode == 'pso':
        pso_evo(args=args, evaluator=evaluator)
    elif args.evo_mode == 'gwo':
        gwo_evo(args=args, evaluator=evaluator)

if __name__ == "__main__":
    args = parse_args()
    run(args)
