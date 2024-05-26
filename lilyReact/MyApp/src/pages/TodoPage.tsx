import React, { useState } from 'react'
import { View, Text } from 'react-native'

import Checkbox from 'expo-checkbox'

// for this kind of non default export, when you import, you need to use braces to import
export const NotDefault = () => {

}

interface TodoItemProps {
    text: string,
    normalColor: string,
    checkedColor: string,
}

const TodoItem: React.FC<TodoItemProps> = ({ text, normalColor, checkedColor }) => {
    const [checked, setChecked] = useState(false)

    return (
        <View style={{ flexDirection: 'row', paddingTop: 20 }}>
            <Checkbox style={{ width: 20, height: 20 }} onValueChange={() => { setChecked(!checked) }} value={checked} />
            <Text style={{ paddingLeft: 20, fontSize: 18, color: checked ? checkedColor : normalColor }}> {text} </Text>
        </View>
    )
}

const TodoList = () => {

    const [items, setItems] = useState(["study for 8 hours", "buy groceries", "eat potato"])

    // <></> fragment
    return (
        <View style={{flexDirection: 'column'}}> 
            <View style={{ paddingTop: 100, padding: 30, backgroundColor: 'white' }}>
                {
                    items.map((x, i) => <TodoItem key={i} text={x} normalColor='black' checkedColor='gray' />)
                }
            </View>

            <Text> ──────────────────────────────</Text>
        </View>
    )
}

// ask GPT how to do this
// when you check a checkbox, change the text of that item to gray


// for default export, when import no need braces
export default TodoList

//npx expo start (in terminal) to start the process

//javascript grammar:
// checked ? 'gray' : 'black'
// ternary operator ?:
// condition ? expression1 : expression2, is a concise way to write conditional statements 
// in many programming languages. It's a shorthand for an if-else statement. Here's how it works:

//condition: This is the expression that evaluates to either true or false.
//expression1: If the condition is true, the value of this expression is returned.
//expression2: If the condition is false, the value of this expression is returned.