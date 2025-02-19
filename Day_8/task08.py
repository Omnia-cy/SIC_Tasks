# Solution_1 : using find ()
#method finds the first occurrence of the specified value.
#and returns -1 if the value is not found.
def Find_Tags_Error(html_contant):
    stack = []
    i = 0
    hc = False # it will return true only if the html contant have error

    while i < len(html_contant):
        if html_contant[i] == "<":
            if html_contant[i + 1] != "/":
                tag_end = html_contant.find(">", i)
                if tag_end != -1:
                    tag = html_contant[i + 1:tag_end]
                    if 'img' in tag or 'meta' not in tag:
                        stack.append(tag)
                        i = tag_end


            else:
                tag_end = html_contant.find(">", i)
                if tag_end != -1:
                    close_tag = html_contant[i + 2:tag_end]
                    if stack and stack[-1] == close_tag or ('img' in close_tag or 'meta' not in close_tag): # stack[-1] mean the top
                        stack.pop()
                    else:
                        print("</",close_tag,"> Not opened tag")
                        hc = True
                    i = tag_end
        i += 1

    while stack:
        print("Opened tag <",stack.pop(),"> Not closed")
        hc = True
    return hc

html_contant = " <html> <head><title><meta charset=UTF-8></title><body><div> </body> </div> </head></html>"
if Find_Tags_Error(html_contant):
    print("Invalid Scenario")
else:
    print("Valid Scenario")
