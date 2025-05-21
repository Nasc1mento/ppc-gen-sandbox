import QtQuick
import QtQuick.Controls 6.0

Window {
    width: 300
    height: 200
    visible: true

    Button {
        text: "Clique e gere"
        onClicked: backend.engine()
        width:300
        height:200
    }
}