import vs

handles = list(())
centerX = 0
layerName = ""
offset = 0

def execute():
        centerX = vs.RealDialog("Please enter the x value of the center of your pipe.", 0)
        vs.TextSize(1)
        vs.ForEachObjectInLayer( getLightLocations, 2, 0, 0)
        #offset = vs.Get2DPt(handles[len(handles) - 1], 0)[0] - vs.Get2DPt(handles[0], 0)[0]
        # if (offset < 0):
        #         offset *= -1
        #center
        vs.DSelectAll()
        for h in handles:
                if centerX < 0:
                        x = vs.Get2DPt(h, 0)[0] + centerX 
                else:
                        x = vs.Get2DPt(h, 0)[0] - centerX 
                vs.MoveTo(x, 0.333 + .192 +.427)
                vs.PenSize(100)
                vs.MoveTo(x,0+.427)
                text = "Instrument: " + vs.LDevice_GetParamStr(h,0, -2, "Inst Type")
                vs.CreateText(text)
                vs.SetTextJust(vs.LNewObj(),2)
                vs.MoveTo(x, -.384+.427)
                text = "U: " + vs.LDevice_GetParamStr(h,0, -2, "Unit Number") + ", C: " + vs.LDevice_GetParamStr(h,0, -2, "Channel")
                vs.CreateText(text)
                vs.SetTextJust(vs.LNewObj(),2)
                vs.MoveTo(x, -.768+.427)
                text = "Dimmer: " + vs.LDevice_GetParamStr(h,0, -2, "Dimmer") + ", Address: " + vs.LDevice_GetParamStr(h,0, -2, "UniverseAddress")
                vs.CreateText(text)
                vs.SetTextJust(vs.LNewObj(),2)
                vs.MoveTo(x, -1.152+.427)
                text = "Color: " + vs.LDevice_GetParamStr(h,0, -2, "Color")
                vs.CreateText(text)
                vs.SetTextJust(vs.LNewObj(),2)
        vs.TextSize(2)
        vs.MoveTo(centerX, 0.333+.427)
        vs.CreateText("C")
        counter = 0
        currentX = -360
        while counter < 40:
                vs.MoveTo(currentX, 0.333 + .192+.427)
                vs.LineTo(currentX, .192+.427)
                currentX += 18
                counter+=1

def getLightLocations(h):
        handles.append(h)
        return False
