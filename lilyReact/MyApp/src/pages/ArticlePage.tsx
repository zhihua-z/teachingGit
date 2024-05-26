import React, { useState } from 'react'
import { View, Text, Image } from 'react-native'

const Article = () => {
    const [profilePhoto, _] = useState('https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo311p0el4qgg005ob911tgktdp4og37jg?imageView2/2/w/120/format/jpg|imageMogr2/strip')
    const [username, _2] = useState('Chiikawaaa')
    return (
        <View>
            <Image style={{ width: '100%', height: 400 }} source={require('../../assets/flower.jpg')} />

            <View style={{padding: 10}}>
                <View style={{ flexDirection: 'row' }}>
                    <Image style={{ width: 50, height: 50, borderRadius: 25}} source={{ uri: profilePhoto }} />
                    <Text style={{ fontSize: 16, color: 'gray', paddingTop: 12.5, paddingLeft: 10}} >{username}</Text>
                </View>
                <Text style={{ fontSize: 24, fontWeight: 700, paddingTop: 10, paddingBottom: 10, color: '#353535'}}>印尼组队7月 华人美女领队</Text>
                <Text style={{ fontSize: 18, fontWeight: 300}} >7月19日 和29日都有团！！美女摄影师用富士可以给大家拍照！！！不特种兵，可以透彻地玩个舒服！现在已经有4个人，都是年轻人，是旅游也是交朋友！！#自由行 我们双火山瀑布➕巴厘岛租别墅游玩 ！！有没有美女帅哥一起的！！！#巴厘岛 #印尼组队 #巴厘岛组队</Text>
                <Text style={{ fontSize: 12, color: 'gray', paddingTop: 10, paddingBottom: 10}}>2024-05-12 重庆</Text>
                <Text style={{ fontWeight: 200 }}>───────────────────────────</Text>
            </View>
        </View>
    )
}

export default Article