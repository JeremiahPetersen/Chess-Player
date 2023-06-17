import chess
import random

def random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

def play_random_chess_game():
    board = chess.Board()
    move_count = 1
    game_moves = []  # EMPTY LIST TO STORE GAME MOVES

    while not board.is_game_over():
        move = random_move(board)
        san_move = board.san(move)  # CONVERT MOVE TO STANDARD ALGEBRAIC NOTATION
        
        if board.turn == chess.WHITE:
            game_moves.append((san_move, None))  # APPEND THE WHITE MOVE AS A TUPLE WITH NONE FOR BLACK MOVE
        else:
            game_moves[-1] = (game_moves[-1][0], san_move)  # REPLACE THE LAST TUPLE WITH THE BLACK MOVE ADDED
        
        board.push(move)
        print(f"{move_count}. {san_move}")
        print(board)
        print("-------------------")
        move_count += 1

    print("Game Over")
    print("Result:", board.result())
    print("\nGame Moves:")  # PRINT THE GAME MOVES
    for i, (white_move, black_move) in enumerate(game_moves, start=1):
        print(f"{i}. {white_move} {black_move if black_move else ''}")

if __name__ == "__main__":
    play_random_chess_game()
