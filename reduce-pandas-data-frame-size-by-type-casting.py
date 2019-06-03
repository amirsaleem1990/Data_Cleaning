def reduce_size_of_vars(dataframe):
	# int8 = -128/127
	# int16 = -32768/32767
	# float16 = -32768/32767
	# float32 = -2147483648 / 2147483647
	# int32 = -2147483648 / 2147483647
	global df
	for i in df.columns:
	    aa = df[i]
	    typ = aa.dtype
	    if typ == "int" or typ == "float":
	        if (aa.min() >= -128) and (aa.max() <= 127):
	            if typ == "int64":
	                df[i] = aa.astype('int8')
	            elif typ == "float64":
	                df[i] = aa.astype('float16')
	        elif (aa.min() >= -32768) and (aa.max() <= 32767):
	            if typ == "int64":
	                df[i] = aa.astype('int16')
	            elif typ == "float64":
	                df[i] = aa.astype('float16')
	        elif (aa.min() >= -2147483648) and (aa.max() <= 2147483647):
	            if typ == "int64":
	                df[i] = aa.astype('int32')
	            elif typ == "float64":
	                df[i] = aa.astype('float32')
	    elif typ == 'O': # string/catagorical variables
	        if (aa.nunique() / len(aa)) < 0.5:
	            df[i] = aa.astype('category')