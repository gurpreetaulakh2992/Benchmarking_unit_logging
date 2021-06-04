import log
# parent classs
class Train():
    def __init__(self, problemNumber, graph):
        # if problem number is less than or gretaer than 10 then message displayed
        # assert problemNumber > 0 and problemNumber <=10, "Problem improperly specified: problem number must be between 0 and 10 "
        self.problem_number = problemNumber
        self.graph = graph
        if not isinstance (problemNumber, int):
            error = f"Problem number should be integer provided: {type(problemNumber)}"
            log.logging.error(error)
            assert False

    def find_all_paths(self):
        pass