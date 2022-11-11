<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>BridgeBeam.py</Name>
        <Title>CreateBridgeBeam</Title>
        <Version>1.0</Version>
    </Script>

    <Page>
        <Name>Page3</Name>
        <Text>Polygon3D</Text>
        
        
        <Parameter>
            <Name>Separator1</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>BeamLength</Name>
            <Text>Довжина опалубка</Text>
            <Value>12000.</Value>
            <MinValue>12000.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>BeamHeight</Name>
            <Text>Загальна висота опалубки</Text>
            <Value>1100.</Value>
            <MinValue>1100.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        
        <Parameter>
            <Name>Separator2</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>TopShWidth</Name>
            <Text>Ширина верхньої полиці</Text>
            <Value>600.</Value>
            <MinValue>600.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>TopShHeight</Name>
            <Text>Висота верхньої полиці</Text>
            <Value>320.</Value>
            <MinValue>320.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>

        <Parameter>
            <Name>Separator3</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
         <Parameter>
            <Name>WidthThick</Name>
            <Text>Товщина центрального ребра</Text>
            <Value>160.</Value>
            <MinValue>160.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>      
        <Parameter>
            <Name>RibHeight</Name>
            <Text>Висота центрального ребра</Text>
            <Value>467.</Value>
            <MinValue>467.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        
        <Parameter>
            <Name>Separator4</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>HoleDepth</Name>
            <Text>Відступ до отвору</Text>
            <Value>350.</Value>
            <MinValue>350.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
        <Parameter>
            <Name>HoleHeight</Name>
            <Text>Висота до отвору</Text>
            <Value>450.</Value>
            <ValueType>Length</ValueType>
        </Parameter>

        <Parameter>
            <Name>Separator5</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
            <Name>BotShWidth</Name>
            <Text>Ширина нижньої полиці</Text>
            <Value>480.</Value>
            <MinValue>480.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
         <Parameter>
            <Name>BotShRectHeight</Name>
            <Text>Висота нижньої полиці(прямокутний блок)</Text>
            <Value>153.</Value>
            <MinValue>153.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>
         <Parameter>
            <Name>BotShTriangHeight</Name>
            <Text>Висота нижньої полиці(трикутний блок)</Text>
            <Value>160.</Value>
            <MinValue>160.</MinValue>
            <ValueType>Length</ValueType>
        </Parameter>     
        
        <Parameter>
            <Name>Separator6</Name>
            <ValueType>Separator</ValueType>
        </Parameter>
        <Parameter>
                <Name>RotationAngleX</Name>
                <Text>Поворот відносно осі X</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationAngleY</Name>
                <Text>Поворот відносно осі Y</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
            <Parameter>
                <Name>RotationAngleZ</Name>
                <Text>Поворот відносно осі Z</Text>
                <Value>0</Value>
                <ValueType>Angle</ValueType>
            </Parameter>
    </Page>    
</Element>
