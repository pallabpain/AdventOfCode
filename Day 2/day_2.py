print "Total wrapping paper =", sum([2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
          for l, w, h in [[int(x) for x in i]
            for i in [i.rstrip('\n').split('x')
                for i in open("input.txt").readlines()]]])

print "Total Ribbon =", sum([ 2*x + 2*y + x*y*z
          for x, y, z in [sorted([int(x) for x in i])
            for i in [i.rstrip('\n').split('x')
                for i in open("input.txt").readlines()]]])