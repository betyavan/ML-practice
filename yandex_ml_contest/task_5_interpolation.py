from sklearn.linear_model import LinearRegression

train_features = []
train_value = []
test_data = []


def get_pair_mult(args: list):
    res = [1]
    for i in range(len(args)):
        for j in range(i, len(args)):
            res.append(args[i] * args[j])
    return res


with open('input.txt') as file:
    for itr in range(1000):
        line = list(map(float, file.readline().split('\t')))
        args = line[:-1]
        value = line[-1]
        train_value.append(value)
        train_features.append(args + get_pair_mult(args))
    for itr in range(1000):
        args = list(map(float, file.readline().split('\t')))
        test_data.append(args + get_pair_mult(args))

model = LinearRegression()
model.fit(train_features, train_value)

with open('output.txt', "w") as file:
    pred = model.predict(test_data)
    file.write('\n'.join(map(str, pred)))
