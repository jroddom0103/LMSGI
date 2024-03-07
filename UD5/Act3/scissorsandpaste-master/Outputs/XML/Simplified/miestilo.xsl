<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text"/>
<xsl:template match="/">
A
 <xsl:comment>Apartado 3.1</xsl:comment>
 <xsl:text>&#xA;</xsl:text>
 <xsl:for-each select="root/record">
 <xsl:value-of select="id"/>
 <xsl:text>. </xsl:text>
 <xsl:value-of select="title"/>
 <xsl:text>: </xsl:text>
 <xsl:value-of select="date/@when"/>
 <xsl:text>&#xA;</xsl:text>
</xsl:for-each>



 B


 <xsl:comment>Apartado 3.2</xsl:comment>
 <xsl:for-each select="root/record">
 <xsl:comment>B</xsl:comment>
 <xsl:text>[</xsl:text>
 <xsl:value-of select="id"/>
 <xsl:text>]</xsl:text>
 <xsl:value-of select="text"/>
 <xsl:text>&#xA;</xsl:text>

</xsl:for-each>


 C


 <xsl:comment>Apartado 3.3</xsl:comment>
 <xsl:for-each select="root/record">
 <xsl:value-of select="title"/>
 <xsl:text>: </xsl:text>
 <xsl:value-of select="date/@when"/>
 <xsl:text>&#xA;</xsl:text>
</xsl:for-each>
 


 D

 <xsl:comment>Apartado 3.4</xsl:comment>
 <xsl:for-each select="root/record">
 <xsl:sort select="date" order="descending" data-type="text"/>
 <xsl:text>&#xA;</xsl:text>
 <xsl:value-of select="date/@when"/>
 <xsl:text>&#xA;</xsl:text>
 <xsl:value-of select="text"/>
</xsl:for-each>


E
 <xsl:comment>Apartado 3.5</xsl:comment>
 <xsl:for-each select="root/record">
 <xsl:sort select="date" order="descending" data-type="text"/>
 <xsl:if test = "date/year &gt;= '1789'">
 <xsl:text>&#xA;</xsl:text>
 <xsl:value-of select="id"/>
 <xsl:text>, </xsl:text>
 <xsl:value-of select="title"/>
 <xsl:text>, </xsl:text>
 <xsl:value-of select="date/@when"/>
</xsl:if>
</xsl:for-each>

</xsl:template>

</xsl:stylesheet>
