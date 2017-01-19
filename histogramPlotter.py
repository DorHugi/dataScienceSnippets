for label in labelsDict:
    if position == 4:
        position = 1
        fig = plt.figure(figsize=(15, 12))
        fig.suptitle('{} histograms'.format(curType), fontsize=22)
        maxOptionsNum = minBars  # Makes sure that are at least minBars at each figure
        graphsList = []

    graphsList.append(plt.subplot(3, 1, position))

    valuesCounter = labelsDict[label]

    # plot attribute:
    labels = valuesCounter.keys()
    values = valuesCounter.values()
    optionsNum = len(valuesCounter)

    # If there are too many options, plotting would be impossible. Therefore we group the least popular options
    if optionsNum > maxBars:
        elemsToRemove = optionsNum - maxBars
        GroupLeastPopular(valuesCounter, elemsToRemove)
        optionsNum = len(valuesCounter)
    plotTitle = label

    indices = np.arange(optionsNum)
    plt.title(plotTitle)
    plt.bar(indices, values)
    plt.xticks(indices, labels, rotation=45)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.tight_layout(h_pad=3.0)
    plt.xlim([0, max(minBars, optionsNum)])  # Makes sure there are at least minBars bars
    position += 1

    # Settings for all subplots:
    plt.subplots_adjust(top=0.90)

plt.show()
