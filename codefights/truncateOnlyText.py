def get_truncated_chunk(text, position):
    counter, open_tag, close_tag, inside_anchor_tag, end_chunk = 0, False, False, False, 0
    for idx, char in enumerate(text):
        if char == '<':
            inside_anchor_tag = True if text[idx+1] == 'a' else False
            if text[idx+1] != '/':
                open_tag = True
            else:
                close_tag = True
        elif open_tag and char == '>':
            open_tag, inside_tag = False, True
        elif close_tag and char == '>':
            close_tag = False
        elif not open_tag and not close_tag:
            counter += 1
        if counter == position:
            end_chunk = idx
            if inside_anchor_tag:
                end_chunk += text[idx+1:].find('>') + 1
            break
    return text[:end_chunk+1]


def truncateOnlyText(text, position):
    truncatedText = get_truncated_chunk(text, position)
    lastTagIndex = truncatedText.rfind('<')
    closedTag = truncatedText[lastTagIndex:].find('>')
    if closedTag == -1 and lastTagIndex != -1:
        lastChunk = truncatedText[lastTagIndex:]
        if '</' in lastChunk:
            openTagBegin = truncatedText[:lastTagIndex].rfind('<')
            truncatedText = truncatedText[:openTagBegin]
        else:
            truncatedText = truncatedText[:lastTagIndex]
    elif lastTagIndex > -1 and closedTag > -1 and truncatedText[lastTagIndex+1] != '/':
        truncatedText = truncatedText[:lastTagIndex] + truncatedText[lastTagIndex + closedTag + 1:]
    print(truncatedText)
    return truncatedText


if __name__ == "__main__":
    input_vars = [
        "You ordered <b>two</b> pizzas with <i>mushrooms</i> and vanilla <i>milkshake</i>.", 50,
        "Lorem ipsum <i>dolor</i> <span>sit</span> amet, <b>eu nonumes facilis</b> reprimique vel, mutat persequeris pri ex.",38,
        "Welcome to the <a href=\"/hotels\">hotel</a> California.", 20,
        "You ordered <b>two</b> pizzas with <i>mushrooms</i> and vanilla <i>milkshake</i>.", 54,
        "<h1>My First Heading</h1><p>My first paragraph.</p>", 11,
        "Welcome to the <a href=\"/hotels\">hotel</a> California.", 4,
        "<h1>My First Heading</h1><p>My first paragraph.</p>", 2
    ]
    output_vars = [
        "You ordered <b>two</b> pizzas with <i>mushrooms</i> and vanilla ",
        "Lorem ipsum <i>dolor</i> <span>sit</span> amet, eu nonumes",
        "Welcome to the <a href=\"/hotels\">hotel</a>",
        "You ordered <b>two</b> pizzas with <i>mushrooms</i> and vanilla milk",
        "My First He",
        "Welc",
        "My"
    ]
    for i, output in zip(range(0, len(input_vars), 2), output_vars):
        print(truncateOnlyText(input_vars[i], input_vars[i+1]) == output)
