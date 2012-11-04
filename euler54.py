#!/usr/bin/env python
def read_file(filename = 'poker.txt'):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def convert_a_to_num(lines):
    new_lines = []
    for line in lines:
        new_line = []
        for item in line.split():
            if item[0] == 'T':
                item = [10] + [item[1]]
            elif item[0] == 'J':
                item = [11] + [item[1]]
            elif item[0] == 'Q':
                item = [12] + [item[1]]
            elif item[0] == 'K':
                item = [13] + [item[1]]
            elif item[0] == 'A':
                item = [14] + [item[1]]
            else:
                item = [int(item[0])] + [item[1]]
            new_line.append(item)

        new_lines.append(new_line)

    return new_lines

def same_color(args):
    color = args[0][1]
    for item in args:
        if item[1] != color:
            return False

    return True

def same_num(args):
    color = args[0][1]
    for item in args:
        if item[1] != color:
            return False

    return True

def same_card(args):
    num = args[0]
    for item in args:
        if item != num:
            return False

    return True

def get_card_num(args):
    return [item[0] for item in args]

def royal_flush(args):
    if not same_color(args):

        return False
    
    card_num = get_card_num(args)
    card_num.sort()
    #print card_num
    if card_num == [10, 11, 12,13, 14]:
        return True
    else:
        return False

def straight_flush(args):
    if len(args) != 5:
        return False

    if not same_color(args):
        return False

    if not consecutive_num(args):
        return False

    max = 0
    nums = get_card_num(args)
    for item in nums:
        if item > max:
            max = item

    return max

def four_of_a_kind(args):
    args = get_card_num(args)
    for item in args:
        if args.count(item) == 4:
            return item
            
    return False

def four_of_a_kind_last_num(args):
    args = get_card_num(args)
    for item in args:
        if args.count(item) == 1:
            return item

def three_of_a_kind(args):
    args = get_card_num(args)
    for item in args:
        if args.count(item) == 3:
            return item
    return False

def rest_of_three_of_a_kind(args):
    result = three_of_a_kind(args)
    nums = get_card_num(args)
    diff = []
    for item in nums:
        if item != result:
            diff.append(item)

    return diff



def consecutive_num(args):
    args = get_card_num(args)
    args.sort()
    for i in xrange(len(args) - 1, 0, -1):
        if args[i] - args[i-1] != 1:
            return False

    return True


def full_house(args):
    result = three_of_a_kind(args)
    if not result:
        return False

    nums = get_card_num(args)
    items = []
    for item in nums:
        if item != result:
            items.append(item)

    if items[0] == items[1]:
        return result, items[0]
    else:
        return False

def flush(args):
    if len(args) == 5 and same_color(args):
        return True
    return False

def straight(args):
    if len(args) == 5 and consecutive_num(args):
        return True
    return False

def get_straight_num(args):
    pass

def two_pairs(args):
    
    pairs = []
    count = 0
    nums = get_card_num(args)
    for item in nums:
        if nums.count(item) == 2:
            count += 1
            pairs.append(item)

    if count == 4: #same item will be counted twice
        return pairs
    else:
        return False

def rest_of_two_pairs(args):
    nums = get_card_num(args)
    for item in nums:
        if nums.count(item) == 1:
            return item

def one_pair(args):
    num = get_card_num(args)
    for item in num:
        if num.count(item) == 2:
            return item
    return False

def rest_of_one_pair(args):
    num = get_card_num(args)
    items = []
    for item in num:
        if num.count(item) == 1:
            items.append(item)

    return items

def score(args):
    if royal_flush(args):
        return 10
    if straight_flush(args):
        return 9
    if four_of_a_kind(args):
        return 8 
    if full_house(args):
        return 7 
    if flush(args):
        return 6
    if straight(args):
        return 5
    if three_of_a_kind(args):
        return 4
    if two_pairs(args):
        return 3
    if one_pair(args):
        return 2
    return 1

def compare_num(args1, args2):
    args1 = get_card_num(args1)
    args2 = get_card_num(args2)

    args1.sort()
    args2.sort()
    for i in reversed(xrange(0, len(args1))):
        if args1[i] > args2[i]:
            return True
        elif args1[i] < args2[i]:
            return False
        else:
            pass

def tests():
    hand = [[10, 'C'], [11, 'C'], [12, 'C'], [13, 'C'], [14, 'C']]
    assert same_color(hand)
    assert straight_flush(hand)
    assert royal_flush(hand) 
    assert straight(hand)

    hand = [[10, 'C'], [11, 'C'], [12, 'C'], [8, 'C'], [9, 'C']]
    assert straight_flush(hand)
    hand = [[10, 'C'], [11, 'C'], [9, 'C'], [8, 'C'], [9, 'C']]
    assert not straight_flush(hand)
    hand = [[10, 'C'], [11, 'D'], [12, 'C'], [8, 'C'], [9, 'C']]
    assert not straight_flush(hand)


    hand = [[10, 'C'], [10, 'C'], [10, 'C'], [13, 'C'], [14, 'C']]
    assert not four_of_a_kind(hand)
    assert three_of_a_kind(hand)
    hand = [[10, 'C'], [10, 'C'], [10, 'C'], [10, 'C'], [14, 'C']]
    assert four_of_a_kind(hand)

    hand = [[10, 'B'], [10, 'C'], [10, 'D'], [12, 'C'], [12, 'C']]
    assert three_of_a_kind(hand)
    assert full_house(hand)

    hand = [[10, 'B'], [10, 'B'], [10, 'B'], [12, 'B'], [12, 'B']]
    assert flush(hand)

    hand = [[9, 'B'], [9, 'B'], [10, 'B'], [10, 'B'], [12, 'B']]
    assert two_pairs(hand)
    hand = [[9, 'D'], [9, 'B'], [10, 'B'], [10, 'B'], [12, 'B']]
    assert two_pairs(hand)
    assert one_pair(hand)

    hand = [[9, 'D'], [1, 'B'], [2, 'B'], [3, 'B'], [12, 'B']]
    assert not one_pair(hand)

    hand = [[5, 'C'], [15, 'D'], [5, 'D'], [15, 'C'], [9, 'C']]
    assert not three_of_a_kind(hand)

    hand1 = [[8, 'C'], [10, 'S'], [13, 'C'], [9, 'H'], [4, 'S']] 
    hand2 = [[7, 'D'], [2, 'S'], [5, 'D'], [3, 'S'], [14, 'C']]
    assert not compare_num(hand1, hand2)

if __name__ == '__main__':
    #print royal_flush('JB', 'KB', 'AB', 'QB', 'TB')
    tests()

    player1_win_count = 0
    player2_win_count = 0
    lines = read_file()
    lines = convert_a_to_num(lines)
    # lines = [[[8, 'C'], [10, 'S'], [14, 'C'], [9, 'H'], [4, 'S'], [7, 'D'], [2, 'S'], [5, 'D'], [3, 'S'], [15, 'C']]]
    for line in lines:
        player1_hand = [line[0], line[1], line[2], line[3], line[4]]
        player2_hand = [line[5], line[6], line[7], line[8], line[9]]
        score1 = score(player1_hand)
        score2 = score(player2_hand)
        if score1 == 8 or score2 == 8:
            print player1_hand, score1, '\n', player2_hand, score2, '\n'
        if score1 > score2:
            player1_win_count +=1
            # print player1_hand, score1, '\n', player2_hand, score2, '\n'
        elif score1 < score2:
            player2_win_count += 1
            #print player1_hand, score1, '\n', player2_hand, score2, '\n'
        else:
            if score1 == 9 and straight_flush(player1_hand) > straight_flush(player2_hand):
                player1_win_count += 1
            elif straight_flush(player1_hand) < straight_flush(player2_hand):
                player2_win_count += 1
                
            if score1 == 8:
                if four_of_a_kind(player1_hand) > four_of_a_kind(player2_hand):
                    player1_win_count += 1
                elif four_of_a_kind(player1_hand) == four_of_a_kind(player2_hand):
                    if four_of_a_kind_last_num(player1_hand) > four_of_a_kind_last_num(player2_hand):
                        player1_win_count += 1
                    else:
                        player2_win_count += 1
                else:
                    player2_win_count += 1

            if score1 == 7:

                result11, result12 = full_house(player1_hand)      
                result21, result22 = full_house(player2_hand)
                if result11 > result21:
                    player1_win_count +=1
                elif result11 == result21 and result12 > result22:
                    player1_win_count += 1
                else:
                    player2_win_count += 1

            if score1 == 6 or score1 == 5:
                if compare_num(player1_hand, player2_hand):
                    player1_win_count += 1
                else:
                    player2_win_count += 1

            if score1 == 4:
                if three_of_a_kind(player1_hand) > three_of_a_kind(player2_hand):
                    player1_win_count += 1
                elif three_of_a_kind(player1_hand) == three_of_a_kind(player2_hand):
                    rest_of_three_of_a_kind_1 = rest_of_three_of_a_kind(player1_hand)
                    rest_of_three_of_a_kind_2 = rest_of_three_of_a_kind(player2_hand)
                    rest_of_three_of_a_kind_1.sort()
                    rest_of_three_of_a_kind_2.sort()
                    for i in reversed(xrange(0, len(rest_of_three_of_a_kind_2))):
                        if rest_of_three_of_a_kind_1[i]>rest_of_three_of_a_kind_2[i]:
                            player1_win_count += 1
                            break
                        elif rest_of_three_of_a_kind_1[i]<rest_of_three_of_a_kind_2[i]:
                            player2_win_count += 1
                            break

                else:
                    player2_win_count += 1

            if score1 == 3:
                pairs1 = two_pairs(player1_hand)
                pairs2 = two_pairs(player2_hand)
                pairs1.sort()
                pairs2.sort()
                if pairs1[1] > pairs2[1]:
                    player1_win_count += 1
                elif pairs1[1] == pairs2[1] and pairs1[0] > pairs2[0]:
                    player1_win_count += 1
                elif pairs1[1] == pairs2[1] and pairs1[0] == pairs2[0]:
                    if rest_of_two_pairs(player1_hand) > rest_of_two_pairs(player2_hand):
                        player1_win_count += 1
                        break
                    else:
                        player2_win_count += 1
                else:
                    player2_win_count += 1
               

            if score2 == 2:
                if  one_pair(player1_hand) > one_pair(player2_hand):
                    player1_win_count += 1

                elif one_pair(player1_hand) == one_pair(player2_hand):
                    rest1 = rest_of_one_pair(player1_hand)
                    rest2 = rest_of_one_pair(player2_hand)
                    rest1.sort()
                    rest2.sort()
                    for i in reversed(xrange(0, len(rest1))):
                        if rest1[i] > rest2[i]:
                            player1_win_count += 1
                            break
                        else:
                            player2_win_count += 1
                            break
                else:
                    player2_win_count += 1

            if score1 == 1:
                if compare_num(player1_hand, player2_hand):
                    player1_win_count += 1
                else:
                    #print player1_hand, score1, '\n', player2_hand, score2, '\n'                    
                    player2_win_count += 1
            # print player1_hand, score1, '\n', player2_hand, score2, '\n'

    print player1_win_count
    print player2_win_count



        
