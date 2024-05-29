import math

class ABMinimaxAgent:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def next_move(self, state=NoughtsAndCrosses()):
        player = state.next_player

        best_action = None
        best_value = -1 * math.inf
        for action in state.actions():
            new_state = state.move(action[0], action[1])
            action_value = self.get_value(new_state, player, get_min=True)
            if self.verbose:
                print(action,value, end=" ")
            if action_value > best_value:
                best_action = action
                best_value = action_value
        if self.verbose:
            print()
        return best_action

    def get_value(self, state, player, get_min, alpha=-math.inf, beta=math.inf):
        """If get_min is set to True, returns the minimum value, otherwise the maximum value"""
        other_player = state.flip_player[player]

        winner = state.winner()
        if winner == player:
            return 1
        elif winner == other_player:
            return -1
        elif winner == state.draw:
            return 0

        best_value = math.inf
        if not get_min:
            best_value *= -1

        for action in state.actions():
            new_state = state.move(action[0], action[1])
            action_value = self.get_value(new_state, player, get_min= not get_min, alpha=alpha, beta=beta)

            if not get_min:
                alpha = max(alpha, action_value)
                if action_value >= beta:
                    return action_value
            else:
                beta = min(beta, action_value)
                if action_value <= alpha:
                    return action_value

            if not get_min and action_value > best_value \
                   or get_min and action_value < best_value:
                best_value = action_value

        return best_value
