from __future__ import division

def rgb_to_hls (r, g, b):
	max_val = max(r,g,b)
	min_val = min(r,g,b)

	l = r*0.2126 + g*0.7152 + b*0.0722
	l = l/255

	if max_val==min_val:
		s = 0
		h = 0
	else:
		if l <= 0.5:
			s = (max_val - min_val) / (max_val + min_val)
		else:
			s = (max_val - min_val) / (2.0 - max_val - min_val)

		delta = max_val - min_val

		if delta == 0:
			delta = 1

		if r == max_val:
			h = (g - b)/delta
		elif g == max_val:
			h = 2.0 + (b - r)/delta
		else:
			h = 4 + (r - g)/delta

		h = h/6

		if h < 0:
			h = h + 1
	
	return [h,l,s]


def hls_to_rgb(h,l,s):
	if s==0:
		r = l*255
		g = l*255
		b = l*255
	else:
		if l<= .5:
			tmp1 = l*(1+s)
		else:
			tmp1 = l + s - l*s

		tmp2 = 2*l - tmp1

                for channel in range(0,3):
                    if channel==0: #red
                        tmpCh = h + 1/3
                    elif channel==1: #green
                        tmpCh = h - 1/3
                    else: #blue
                        tmpCh = h
                    
                    if 6*tmpCh < 1:
                        Ch = tmp2 + (tmp1 + tmp2)*6*tmpCh
                    elif 2*tmpCh < 1:
                        Ch = tmp1
                    elif 3*tmpCh < 2:
                        Ch = tmp2 + (tmp1 - tmp2)*(2/3 - tmpCh)*6
                    else:
                        Ch = tmp2

                    if channel==0:
                        r = Ch
                    elif channel==1:
                        g = Ch
                    else:
                        b = Ch
        
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        return [r, g, b]

