def solution(ip_string):
      ips = []
      for i in range(1, min(len(ip_string), 4)): # -> since a IP segment has at least 1 element, and at most 4
            currentIPAddress = ['', '', '', '']
            currentIPAddress[0] = ip_string[:i]

            if not isValidIP(currentIPAddress[0]):
                  continue # Doesnt make seanse to continue with a invalid IP segment
                  #       i + 1
                  #     i |
                  # X X X X X X 
                  #       |---|
                  #       ip - i
            for j in range(i + 1, i + min(len(ip_string) - i, 4)):
                  currentIPAddress[1] = ip_string[i: j]
                  if not isValidIP(currentIPAddress[1]):
                        continue
                  
                  for k in range(j + 1, j + min(len(ip_string) - j, 4)):
                        currentIPAddress[2] = ip_string[j: k]
                        currentIPAddress[3] = ip_string[k:]

                        if isValidIP(currentIPAddress[2]) and isValidIP(currentIPAddress[3]):
                              ips.append('.'.join(currentIPAddress))
            
            return ips
            

    

def isValidIP(string):
    fragment = int(string)
    if fragment > 255:
            return False
    return len(string) == len(str(fragment))