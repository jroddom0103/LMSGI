<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet>
<xsl:stylesheet version="2.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8"/>
<xsl:template match="/notas">
<html>
    <head>
        <h1 class="azul1" style="margin: 0 auto; text-align: center;">Notas del curso</h1>

        <style type="text/css">
        
        td, th{
            border: black 1px solid;
        }
        .azul1{color:#050799;}
        .azul2{color:#008099;}
        .verde1{color:#009900;}
        .naranja1{color:#FF8000;}
        .rojo1{color:#990000;}
        td{text-align}
        </style>
    </head>  
    <body>

    <div style="text-align: center;  margin: 0 auto;">    

        <h2 class="azul2">Notas de la convocatoria de Junio</h2>
        
        <table style="border-collapse: collapse; margin: 0 auto;">
            

            <tr>
                <th colspan="2">Datos</th>
                <th colspan="4">Notas</th> 
            </tr>    

            <tr>
                <th>Nombre</th>
                <th>Apellidos</th>
                <th>Cuestionarios</th>
                <th>Tareas</th>
                <th>Examenes</th>
                <th>Tipo Nota</th>
            </tr>

            <xsl:for-each select="alumno">
                
                <xsl:if test="@convocatoria = 'Junio'">
            
                <tr>
                    <td><xsl:value-of select="nombre"/></td>
                    <td><xsl:value-of select="apellidos"/></td>
                    <td><xsl:value-of select="cuestionarios"/></td>
                    <td><xsl:value-of select="tareas"/></td>
                    <td><xsl:value-of select="examen"/></td>

                <td>    
                    <xsl:choose>
                    <xsl:when test="number(final) >= 9">
                        <span class="azul1">Sobresaliente</span>
                    </xsl:when>
                    <xsl:when test="number(final) >= 7">
                        <span class="azul2">Notable</span>
                    </xsl:when>
                    <xsl:when test="number(final) >= 6">
                        <span class="verde1">Bien</span>
                    </xsl:when>
                    <xsl:when test="number(final) >= 5">
                        <span class="naranja1">Suficiente</span>
                    </xsl:when>
                    <xsl:otherwise>
                        <span class="rojo1">Suspenso</span>
                    </xsl:otherwise>
                    </xsl:choose>
                                       
                </td>

                </tr>

                </xsl:if>

            </xsl:for-each>

        </table>

    </div>

    </body>
</html>
</xsl:template>
</xsl:stylesheet>