<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <body>
        <h1>Discos de música</h1>
        <table bgcolor="#775522">
            <tr bgcolor="#885588">
                <th>Títulos de las canciones</th>  
            </tr>    
            <xsl:for-each select="cds/cd">
            <xsl:if test="tituloCancion/@tiempo &lt; 150">
            <tr>
                <td><xsl:value-of select="tituloCancion"/></td>
            </tr>
            </xsl:if>
            <xsl:if test="tituloCancion2/@tiempo &lt; 150">
            <tr>
                <td><xsl:value-of select="tituloCancion2"/></td>
            </tr>    
            </xsl:if>
            </xsl:for-each>
        </table>
    </body>
</html>
</xsl:template>
</xsl:stylesheet>
