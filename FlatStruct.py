struct_pos_map = []
Lines = []
New_Lines = []


def find_struct_pos(struct_name):
    for pos in struct_pos_map:
        start_line_num = pos[0]
        if (Lines[start_line_num].__contains__(struct_name)):
            return pos
    return []


def get_struct_content(struct_pos):
    if not struct_pos:
        return ""
    content = ""
    start = struct_pos[0] + 1
    end = struct_pos[1]
    for i in range(start, end):
        content += Lines[i]
    return content


def get_add_flat_struct_content(pos):
    # handle last struct
    start_pos = pos[0]
    end_pos = pos[1] + 1
    new_struct_name = Lines[start_pos].split(" ")[-2] + "Flat"
    tmp_lines = []
    is_need_flat = False
    for i in range(start_pos, end_pos):
        # print(Lines[i])
        line = Lines[i]
        if i == start_pos:
            tmp_lines.append("struct " + new_struct_name + "{\n")
        elif line.__contains__("struct") & (not line.__contains__("{")):
            is_need_flat = True
            # print(i)
            struct_name = line.split(" ")[-2]

            # first find if exist already flat struct
            target_struct_pos = find_struct_pos(struct_name + "Flat")
            if not target_struct_pos:
                target_struct_pos = find_struct_pos(struct_name)

            content = get_struct_content(target_struct_pos)
            # print(content)
            tmp_lines.append(content)
        else:
            tmp_lines.append(line)

    if is_need_flat:
        return tmp_lines
    else:
        return []


if __name__ == "__main__":

    file1 = open('mystruct.h', 'r')
    Lines = file1.readlines()

    struct_begin_line = -1
    struct_end_line = -1
    for line_num, line in enumerate(Lines):
        # print(line)

        if line.startswith("struct ") & line.__contains__("{"):
            struct_begin_line = line_num

        if line.startswith("};"):
            struct_end_line = line_num

        if struct_begin_line != -1 & struct_end_line != -1:
            struct_pos_map.append([struct_begin_line, struct_end_line])
            struct_begin_line = -1
            struct_end_line = -1

    add_flat_structs = []
    for pos in struct_pos_map:
        # print(pos)
        flat_struct = get_add_flat_struct_content(pos)
        if flat_struct:
            add_flat_structs.append(flat_struct)

    add_flat_struct_pos = struct_pos_map[-1][1] + 1

    New_Lines = Lines[0:add_flat_struct_pos]
    for item in add_flat_structs:
        New_Lines.extend(item)

    New_Lines += Lines[add_flat_struct_pos:]

    # save to file
    file1 = open('myfile.txt', 'w')
    file1.writelines(New_Lines)
    file1.close()
