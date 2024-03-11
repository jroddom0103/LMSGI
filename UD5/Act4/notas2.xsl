<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet>
<xsl:stylesheet version="2.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8"/>
<xsl:template match="/notas">
<html>
    <head>
        <h1>Notas del curso</h1>

        <style type="text/css">
        
        td, th{
            border: black 1px solid;
        }
        .azul1{background-color:#369;}
        td{text-align}
        </style>
    </head>  
    <body>

        <h2>Notas de la convocatoria de Junio</h2>
        
        <table border-collapse="collapse">
            
            <tr>
                <th colspan="3">Datos</th>
                <th colspan="3">Notas</th> 
            </tr>    

            <xsl:for-each select="alumno">
                
                <xsl:if test="@convocatoria = 'Junio'">
            
                <tr>
                    <td><xsl:value-of select="nombre"/></td>
                    <td><xsl:value-of select="apellidos"/></td>
                    <td><xsl:value-of select="matricula"/></td>
                    <td><xsl:value-of select="cuestionarios"/></td>
                    <td><xsl:value-of select="examen"/></td>
                    
                    <xsl:choose>
                        <xsl:when test="number(final) >= 9">
                            
                        </xsl:when>
                        <xsl:when test="number(final) >= 7">
                            
                        </xsl:when>
                        <xsl:when test="number(final) >= 6">Bien</xsl:when>
                        <xsl:when test="number(final) >= 5">Suficiente</xsl:when>
                        <xsl:otherwise>Suspenso</xsl:otherwise>
                    </xsl:choose>
                                       
                </tr> 

                </xsl:if>
            </xsl:for-each>

        </table>

    </body>
</html>
</xsl:template>
</xsl:stylesheet>