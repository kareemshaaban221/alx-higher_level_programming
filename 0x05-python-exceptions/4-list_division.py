#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    tmp = None
    for i in range(list_length):
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            tmp = 0
        except TypeError:
            print("{}".format("wrong type"))
            tmp = 0
        except ValueError:
            print("{}".format("wrong type"))
            tmp = 0
        except IndexError:
            print("{}".format("out of range"))
            tmp = 0
        finally:
            res.append(tmp)
    return res
