## Latent Factor Model
class LFM implements Latent factorization of data for recommender systems.
Loss function : Mean squared error('mse')

Predicted Rating 
\hat{R}<sub>ui</sub> = \alpha + \beta<sub>u</sub> + \beta<sub>i</sub> + \gamma<sub>u</sub> + \gamma<sub>i</sub>
MSE function : \sum_{u,i}(R<sub>ui</sub> - \hat{R<sub>ui</sub>})^2 + reg( \beta<sub>u</sub>^2 + \beta<sub>i</sub>^2 + \gamma<sub>u</sub>^2 + \gamma<sub>u</sub>^2)


### Dependencies: 
1. numpy
2. pandas
3. progressbar
4. matplotlib

### Class Definition:
1. Model Definition
   model = LFM()
   Supported params:
   * data : pandas Dataframe
   * nComponents : number of latent factor components(for \gamma<sub>u</sub> and \gamma<sub>i</sub>). default = 10
   * userID      : title in data(pandas) for the userID column. default = 'userID'
   * itemID      : title in data(pandas) for the itemID column. default = 'businessID'
   * target      : title in data(pandas) for the rating column. default = 'rating'
   * timeStamp   : title in data(pandas) for the timeStamp column. default = 'unixReviewTime'
   * mean/std    : mean/std value for the normal initialization of \gamma<sub>u</sub> and \gamma<sub>i</sub>
   * reg         : regularizer value for the learned weights(\beta<sub>u</sub>, \beta<sub>i</sub>, \gamma<sub>u</sub>, \gamma<sub>i</sub>). default = 0.01
   * split_percent: split percentage between train and validation set.   default = 0.6(60% training data - 40% validation data)
   * tGrad       : parameter to capture the linear trend in rating vs time. default = 0.01 (This can be interpreted as rating = tGrad * timeOfRating. For this, timeOfRating has to be transformed into a reasonable value, i.e. ~ 5-50. UnixTimeStamp cannot be used)


2. Available API's 
	* userList, bussList = model.getUniqueUserBusinessList()
   			return Value : Returns two list of unique user and business in all data - as provided to the class consructor

   	* userIndexDict, bussIndexDict = model.getUserBussIndexDict()
   			return Value: two dictionary, mapping every user/business(string) to an integer value(unique for each user)

   	* userInfoDict, bussInfoDict = model.getUserBussInfoDict()
   			return Value: 	two dict corresponding to user/item
   							dict - key : userID/itemID
   							dict - value : a list corresponding to each user/itemID, each element is a sublist - corresponds to each user-item pair or item-user pair
   							The sublist contains information: 
   							userID = 'A12345'
   							userIndex = userIndexDict[userID]
   							userInfoDict[userIndex] = [ [bussIndex1, bussRating1, timeStamp1], [bussIndex2, bussRating2, timeStamp2] , [bussIndex3, bussRating3, timeStamp3] ]

   	* initializeParams : model.initializeParams()
   			To initialize all the weights
   			* \alpha : mean value of all the rating
   			* \beta<sub>u/i</sub> : mean rating deviation for that user/item from the overall mean
   			* \gamma<sub>u/i</sub>: normal distributed from the mean/std initialized in contructor
   			* This function needs to be called before training the model if we dont have an already trained weights for the model(from previous training)

   	* loadParams    : model.loadParams( paramDict )
   			* Initialize the model params with the explicitly provided weights
   			* paramDict : dictionary with key value pair corresponding to all the weights
   			* This function is called in alternative to initializeParams() before model training

   	* predictRatingFromID(self, userID, bussID, timeStamp = 0)
   			* To predict a rating for the user-item pair.

   	* calculateLoss(self, testData ):
   			To calculate 'mse' loss on the provided testData

   	* printBestParams(self):
   			prints best parameters for the trained Model

   	* plotGraph(self):
   	        plots training/validation mse from the last training of the model.
   	        Works even if the training was interrupted in the middle.

   	* train(nEpochs = 50, verbose = True)
   			nEpochs : number of Epochs to train the model
   			verbose : True - prints train/valid loss for each epoch
   			          False- progress bar status for training.

   	* bestParams(self)
   			returns bestParams from the last training in dictionary format. This can be directly used with loadParams(paramDict)

3. Optimization algorithm:
	* The model is trianined using Alternate-least squared. 
	* Some inaccuracies persist in the update rule for \gamma^{prime}, however practically it seems to work fine. 


   						

4. Usage Model 
	* Declare model
	    model = LFM(df_data, reg = 4, nComponents = 1, split_percent = 1)
	* Initialize params or load best params
		model.initializeParams()
		model.loadParams(bestParams)
	* model.train( nEpochs = 50, verbose = True )
	* model.printBestParams()
	* bestParams = model.bestParams()
	* model.plotGraph()



